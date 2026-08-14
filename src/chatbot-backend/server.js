const express = require("express");
const path = require("path");
const fs = require("fs");
require("dotenv").config();

const { GoogleGenAI } = require("@google/genai");

const app = express();
const PORT = process.env.PORT || 3000;

const API_KEY = process.env.GEMINI_API_KEY;
const MODEL = process.env.GEMINI_MODEL || "gemini-3.1-flash-lite";
const SYSTEM_PROMPT =
  process.env.SYSTEM_PROMPT ||
  "You are a helpful and concise Northstar Retail customer support assistant.";

if (!API_KEY) {
  console.error("Missing GEMINI_API_KEY in .env");
  process.exit(1);
}

const ai = new GoogleGenAI({ apiKey: API_KEY });

// Load Northstar JSON database
const databasePath = path.join(__dirname, "data", "northstar_data.json");
const database = JSON.parse(fs.readFileSync(databasePath, "utf8"));

app.use(express.json({ limit: "1mb" }));
app.use(express.static(path.join(__dirname, "public")));

// Find relevant information in the Northstar database
function findDatabaseInfo(messages) {
  const lastMessage = messages[messages.length - 1];

  if (!lastMessage || lastMessage.role !== "user") {
    return "";
  }

  const question = lastMessage.content.toLowerCase();

  // Look for an order ID, e.g. NS-1001
  const orderMatch = question.match(/ns-\d+/i);

  if (orderMatch) {
    const orderId = orderMatch[0].toUpperCase();

    const order = database.order_status.find(
      (item) => item.order_id === orderId
    );

    if (order) {
      return `
Relevant order information from the Northstar database:
${JSON.stringify(order, null, 2)}
`;
    }
  }

  // Look for a return ID, e.g. RET-2003
  const returnMatch = question.match(/ret-\d+/i);

  if (returnMatch) {
    const returnId = returnMatch[0].toUpperCase();

    const returnData = database.returns.find(
      (item) => item.return_id === returnId
    );

    if (returnData) {
      return `
Relevant return information from the Northstar database:
${JSON.stringify(returnData, null, 2)}
`;
    }
  }

  // Search products by name
  const product = database.stock_availability.find((item) =>
    question.includes(item.product_name.toLowerCase())
  );

  if (product) {
    return `
Relevant stock information from the Northstar database:
${JSON.stringify(product, null, 2)}
`;
  }

  return "";
}

// POST /api/chat
app.post("/api/chat", async (req, res) => {
  const { messages } = req.body;

  if (!Array.isArray(messages) || messages.length === 0) {
    return res.status(400).json({
      error: "messages must be a non-empty array"
    });
  }

  try {
    const databaseInfo = findDatabaseInfo(messages);

    const systemInstruction = `
${SYSTEM_PROMPT}

You are connected to the Northstar Retail Co. database.

When database information is provided below:
- Use it to answer the user's question accurately.
- Do not invent or change database information.
- If the database information does not answer the question, say that you do not have enough information.
- Do not expose unnecessary customer personal information.

${databaseInfo}
`;

    const contents = messages.map((message) => ({
      role: message.role === "assistant" ? "model" : "user",
      parts: [{ text: message.content }]
    }));

    const response = await ai.models.generateContent({
      model: MODEL,
      contents,
      config: {
        systemInstruction: systemInstruction
      }
    });

    res.json({
      reply: response.text
    });

  } catch (err) {
    console.error("Gemini API error:", err);

    res.status(502).json({
      error: "Gemini API error",
      detail: err.message
    });
  }
});

app.listen(PORT, () => {
  console.log(`Chatbot server running at http://localhost:${PORT}`);
});
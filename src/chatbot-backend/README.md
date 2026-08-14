# Chatbot with backend

A small chat app: a static front-end (`public/index.html`) talks to your own
Express server (`server.js`), which holds the Anthropic API key and forwards
requests to Claude. The key never reaches the browser, so it's safe to
deploy publicly.

## Setup

1. Install dependencies:
   ```
   npm install
   ```

2. Create your environment file:
   ```
   cp .env.example .env
   ```
   Then open `.env` and paste in your real API key from
   https://console.anthropic.com/settings/keys.

3. Start the server:
   ```
   npm start
   ```

4. Open http://localhost:3000 in your browser. The chatbot can now answer
   whatever you ask it, since it's calling the full Claude model with no
   topic restrictions — the only guardrails are Claude's own built-in ones.

## Deploying it for real

- Set `ANTHROPIC_API_KEY` as an environment variable on your host (Render,
  Railway, Fly.io, a VPS, etc.) rather than shipping the `.env` file.
- Put the server behind HTTPS.
- Consider adding rate limiting (e.g. the `express-rate-limit` package) so
  one visitor can't run up your API bill.
- If you want multiple people to have separate conversations, track
  `conversationHistory` per session (e.g. keyed by a session cookie or user
  ID) server-side instead of trusting the client to send it — the current
  version trusts the browser's copy, which is fine for a personal/demo tool
  but not for a multi-user production app.

## Customizing

- Change `SYSTEM_PROMPT` in `.env` to give the bot a persona or instructions.
- Change `ANTHROPIC_MODEL` in `.env` to use a different model.
- Edit `public/index.html` for styling/UI changes.

## Files

- `server.js` — Express server, holds the API key, exposes `POST /api/chat`
- `public/index.html` — the chat UI, calls `/api/chat` on your own domain
- `.env.example` — template for required environment variables
- `package.json` — dependencies (`express`, `dotenv`)

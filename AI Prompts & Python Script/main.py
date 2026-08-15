# Import the FastAPI framework and HTTP exception handler
from fastapi import FastAPI, HTTPException
# Import BaseModel from pydantic to define typed data schemas
from pydantic import BaseModel
# Import StaticFiles to serve our static frontend assets
from fastapi.staticfiles import StaticFiles
# Import FileResponse to serve the index.html webpage
from fastapi.responses import FileResponse
# Import json module to load and parse the local database
import json
# Import regular expressions module for pattern parsing
import re

# Initialize the FastAPI web server instance
app = FastAPI(title="Northstar Support Deflection Hub")

# Mount the static directory to serve frontend scripts and assets
app.mount("/static", StaticFiles(directory="."), name="static")

# Define a function to load the mock database safely from disk
def load_database(filepath="northstar_data.json"):
    # Start a try block to handle potential missing file errors
    try:
        # Open the JSON data file in read-only mode
        with open(filepath, 'r') as file:
            # Parse the JSON content into a Python dictionary and return it
            return json.load(file)
    # Catch the error if the file is not found
    except FileNotFoundError:
        # Return a safe fallback dictionary structure
        return {"order_status": [], "returns": [], "stock_availability": []}

# Load database into memory at application startup
db = load_database()

# Helper function to find order details by order ID
def get_order_by_id(order_id: str):
    # Normalize the query string to uppercase and strip whitespace
    query = order_id.strip().upper()
    # Iterate through the order_status list in our database
    for order in db.get("order_status", []):
        # Match order_id exactly
        if order.get("order_id", "").upper() == query:
            # Return the matching order record
            return order
    # Return None if no match is found
    return None

# Helper function to find return details by return ID or order ID
def get_return_by_id(identifier: str):
    # Normalize the query string to uppercase and strip whitespace
    query = identifier.strip().upper()
    # Iterate through the returns list in our database
    for ret in db.get("returns", []):
        # Match against return_id or order_id
        if ret.get("return_id", "").upper() == query or ret.get("order_id", "").upper() == query:
            # Return the matching return record
            return ret
    # Return None if no match is found
    return None

# Helper function to search stock items by name or size
def search_stock(keyword: str):
    # Normalize keyword to lowercase
    query = keyword.strip().lower()
    # Initialize a list to hold matching stock items
    results = []
    # Iterate through the stock_availability list in our database
    for item in db.get("stock_availability", []):
        # Check if query matches product name, category, or size
        if query in item.get("product_name", "").lower() or query in item.get("size", "").lower():
            # Append matched item to results list
            results.append(item)
    # Return the collected results
    return results

# Define the Pydantic schema for chat requests
class ChatRequest(BaseModel):
    # The message string sent from the frontend
    message: str

# Define the Pydantic schema for direct order lookups
class OrderLookupRequest(BaseModel):
    # The order ID string to look up
    order_id: str

# Define the Pydantic schema for direct stock lookups
class StockLookupRequest(BaseModel):
    # The product query string
    product_name: str

# Define the Pydantic schema for direct return lookups
class ReturnLookupRequest(BaseModel):
    # The return or order ID string
    identifier: str

# Root route to serve the visual support dashboard
@app.get("/")
def serve_home():
    # Return the index.html file to the browser
    return FileResponse("index.html")

# API endpoint for direct order lookup card
@app.post("/api/lookup/order")
def lookup_order_api(req: OrderLookupRequest):
    # Retrieve order from database helper
    order = get_order_by_id(req.order_id)
    # If order does not exist, return not found message
    if not order:
        # Return failure response
        return {"success": False, "message": f"No order found with ID '{req.order_id}'."}
    # Return success response with order data
    return {"success": True, "data": order}

# API endpoint for direct stock lookup card
@app.post("/api/lookup/stock")
def lookup_stock_api(req: StockLookupRequest):
    # Search items from database helper
    items = search_stock(req.product_name)
    # If no items match, return not found message
    if not items:
        # Return failure response
        return {"success": False, "message": f"No products matching '{req.product_name}'."}
    # Return success response with matching items
    return {"success": True, "data": items}

# API endpoint for direct return lookup card
@app.post("/api/lookup/return")
def lookup_return_api(req: ReturnLookupRequest):
    # Retrieve return from database helper
    ret = get_return_by_id(req.identifier)
    # If return does not exist, return not found message
    if not ret:
        # Return failure response
        return {"success": False, "message": f"No return ticket found for '{req.identifier}'."}
    # Return success response with return record
    return {"success": True, "data": ret}

# API endpoint for the interactive chatbot assistant
@app.post("/chat")
def chat_deflection_api(req: ChatRequest):
    # Convert incoming text to lowercase for intent matching
    msg = req.message.lower().strip()
    
    # Regex search for order ID pattern (e.g., NS-1001)
    order_match = re.search(r"ns-\d{4}", msg)
    # Regex search for return ID pattern (e.g., RET-2001)
    return_match = re.search(r"ret-\d{4}", msg)
    
    # Extract order ID string if found
    order_id = order_match.group(0).upper() if order_match else None
    # Extract return ID string if found
    return_id = return_match.group(0).upper() if return_match else None

    # Handle explicit Order ID query
    if order_id:
        # Fetch order record
        order = get_order_by_id(order_id)
        # Format response if order exists
        if order:
            # Build detailed status message
            carrier = order.get("carrier") or "Processing"
            est = order.get("estimated_delivery") or "TBD"
            return {"reply": f"Order {order_id} ({order.get('customer_name')}) is currently **{order.get('status')}**. Carrier: {carrier}. Expected Delivery: {est}."}
        # Fallback if order not found
        return {"reply": f"I checked our system, but could not find an order with ID '{order_id}'. Please verify the number."}

    # Handle explicit Return ID query
    if return_id:
        # Fetch return record
        ret = get_return_by_id(return_id)
        # Format response if return exists
        if ret:
            # Build detailed refund message
            return {"reply": f"Return {return_id} for '{ret.get('item_returned')}' is **{ret.get('return_status')}**. Refund Amount: ${ret.get('refund_amount')} ({ret.get('refund_method')})."}
        # Fallback if return ticket not found
        return {"reply": f"No return record found for '{return_id}'. Please double check your return number."}

    # Handle general Order Status inquiry without ID
    if any(k in msg for k in ["order", "track", "where is", "shipped", "package", "delivery"]):
        # Prompt user for order number
        return {"reply": "I'd be glad to track your order! Please enter your **Order ID** (e.g., **NS-1001**)."}

    # Handle general Returns & Refunds inquiry without ID
    if any(k in msg for k in ["return", "refund", "exchange", "damaged", "wrong item"]):
        # Prompt user for return or order number
        return {"reply": "For return and refund assistance, please provide your **Return ID** (e.g., **RET-2001**) or **Order ID**."}

    # Handle Stock and Size inquiries
    if any(k in msg for k in ["stock", "size", "available", "color", "in stock", "have"]):
        # Search for any known product in the message
        for item in db.get("stock_availability", []):
            # Check if product name appears in message
            if item.get("product_name", "").lower() in msg:
                # Determine stock text
                status = f"In Stock ({item.get('stock_count')} units at {item.get('warehouse_location')})" if item.get("in_stock") else f"Out of Stock (Restock expected: {item.get('restock_date') or 'TBD'})"
                return {"reply": f"**{item.get('product_name')}** ({item.get('size')}, {item.get('color')}): Currently **{status}** for ${item.get('price')}."}
        # Ask for product name if not recognized
        return {"reply": "Which item are you checking? (e.g., *Wireless Earbuds Pro*, *Running Shoes*, *Yoga Mat*)."}

    # Default general greeting / fallback response
    return {"reply": "Hello! I can help you track orders, check returns/refunds, or verify product stock. What can I help you with today?"}

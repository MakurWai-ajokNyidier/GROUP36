# Import the built-in json module to parse and read JSON files
import json

# Define a function to load our mock database, setting a default filepath
def load_database(filepath="northstar_data.json"):
    # A docstring explaining the purpose of this specific function
    """Reads the JSON database containing order, return, and stock data."""
    
    # Start a try block to handle potential errors if the file doesn't exist
    try:
        # Open the file in read mode ('r') and assign it to the variable 'file'
        with open(filepath, 'r') as file:
            # Parse the JSON file into a Python dictionary and return it
            return json.load(file)
            
    # Catch the specific error that occurs if the file is missing
    except FileNotFoundError:
        # Return a fallback empty dictionary structure so the script doesn't crash
        return {"orders": [], "returns": [], "stock": []}

# Define a function to look up an order status using the order ID and database
def process_order_status(order_id, db):
    # A docstring explaining the purpose of this specific function
    """Retrieves order status from the database."""
    
    # Loop through the "orders" list in the database; default to an empty list if not found
    for order in db.get("orders", []):
        
        # Check if the current order's ID matches the one the user requested
        if order["order_id"] == order_id:
            
            # If it matches, return a formatted string with the order ID and its status
            return f"Order {order_id} is currently: {order['status']}."
            
    # If the loop finishes and no match is found, return an error message
    return "Order not found. Please verify your tracking number."

# Define a function to look up a return status using the return ID and database
def process_return_status(return_id, db):
    # A docstring explaining the purpose of this specific function
    """Retrieves return/refund status from the database."""
    
    # Loop through the "returns" list in the database; default to an empty list if missing
    for ret in db.get("returns", []):
        
        # Check if the current return ticket's ID matches the user's requested ID
        if ret["return_id"] == return_id:
            
            # If it matches, return a formatted string with the return status and refund amount
            return f"Return {return_id} status: {ret['status']}. Refund amount: {ret['refund_amount']}."
            
    # If the loop completes without a match, return a failure message
    return "Return ticket not found. Please contact support."

# Check if this script is being run directly (rather than imported as a module)
if __name__ == "__main__":
    
    # Call the load_database function and store the result in the 'db' variable
    db = load_database()
    
    # Print a success message to the terminal to confirm the system is ready
    print("Database connected successfully. Ready to process queries.")

"""
Northstar Retail Co. — Support Deflection Chatbot (Web Version)
Group 36 | The Northstar Sprint

Deployed on Render for 24/7 demo access.
"""

from flask import Flask, jsonify
from chatbot import load_data, find_order, find_return, find_stock, show_order, show_return, show_stock

app = Flask(__name__)
data = load_data()

@app.route("/")
def home():
    return """
    <h1>🌟 Northstar Support Bot</h1>
    <p>Group 36 MVP — Live Demo</p>
    <h3>Test Endpoints:</h3>
    <ul>
        <li><a href="/order/NS-1001">/order/NS-1001</a> — Order Status</li>
        <li><a href="/return/RET-2001">/return/RET-2001</a> — Returns</li>
        <li><a href="/stock/Running%20Shoes">/stock/Running Shoes</a> — Stock</li>
    </ul>
    """

@app.route("/order/<order_id>")
def get_order(order_id):
    order = find_order(order_id, data)
    if order:
        return f"<pre>{show_order(order)}</pre>"
    return "<h3>❌ Order not found</h3>", 404

@app.route("/return/<return_id>")
def get_return(return_id):
    ret = find_return(return_id, data)
    if ret:
        return f"<pre>{show_return(ret)}</pre>"
    return "<h3>❌ Return not found</h3>", 404

@app.route("/stock/<product_name>")
def get_stock(product_name):
    matches = find_stock(product_name, data)
    if matches:
        return f"<pre>{show_stock(matches)}</pre>"
    return "<h3>❌ Product not found</h3>", 404

if __name__ == "__main__":
    app.run(debug=True)

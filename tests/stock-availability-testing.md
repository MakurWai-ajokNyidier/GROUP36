# Stock Availability Testing

## Test 1: Product In Stock

- **Test:** Enter a valid product that is currently in stock.
- **Expected:** The system confirms that the product is available and shows the available quantity.
- **Actual:** The system correctly identified Yoga Mat Premium (6mm thick, Purple) as in stock, with 23 units available at Nairobi Central, and displayed the price as $35.0.
- **Result:** PASS
- **Evidence:**

## Test 2: Product Out of Stock

- **Test:** Enter a valid product that is currently out of stock.
- **Expected:** The system clearly informs the user that the product is out of stock.
- **Actual:** The system correctly identified Running Shoes Size 42 (42 EU, Blue/White) as out of stock and provided the expected restock date of 2026-08-20.
- **Result:** PASS
- **Evidence:**

## Test 3: Invalid Product

- **Test:** Enter a product name or product ID that does not exist.
- **Expected:** The system gives a clear message that the product could not be found.
- **Actual:** The system did not identify Galaxy Flying Shoes as an invalid or unavailable product. Instead, it asked the user to select a recognized item, providing examples such as Wireless Earbuds Pro, Running Shoes, and Yoga Mat.
- **Result:** FAIL
- **Evidence:**

## Test 4: Empty Product Input

- **Test:** Submit without entering a product name or product ID.
- **Expected:** The system asks the user to enter a product name or product ID.
- **Actual:** The Send button did not respond when the product input was left empty, preventing the user from submitting an empty product request.
- **Result:** FAIL
- **Evidence:**

## Test 5: Different Product Search

- **Test:** Search for another valid product.
- **Expected:** The system returns the correct stock availability for the selected product.
- **Actual:** The system correctly identified Laptop Stand Aluminum (15-inch compatible, Silver) as in stock, with 67 units available at Nairobi Central, and displayed the price as $55.0.
- **Result:** PASS
- **Evidence:**
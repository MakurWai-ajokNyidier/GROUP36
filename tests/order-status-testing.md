## Test 1: Valid Order Status

- **Test:** Enter a valid order number.
- **Expected:** The system returns the correct order status.
- **Actual:** The system correctly identified order NS-1006 as Delivered and provided the carrier and expected delivery date.
- **Result:** PASS
- **Evidence:**

## Test 2: Invalid Order Number

- **Test:** Enter an invalid/non-existent order number.
- **Expected:** The system gives a clear error message.
- **Actual:** The system could not find order NS-1008 and clearly informed the user that the order could not be found, advising them to verify the number.
- **Result:** PASS
- **Evidence:** 

## Test 3: Empty Order Number

- **Test:** Submit without entering an order number.
- **Expected:** The system asks the user to enter an order number.
- **Actual:** The Send button did not respond when the order number field was left empty, preventing the user from submitting the request.
- **Result:** FAIL
- **Evidence:**
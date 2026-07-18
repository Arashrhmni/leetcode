#Question 3 - Clean and Validate Orders
#You have a list of order dictionaries. Some have missing or null fields.
# Write a function that returns a cleaned list where: missing country becomes
# "unknown", missing value becomes 0, any order with no order_id gets removed entirely.

def clean_orders(orders: list[dict]) -> list[dict]:
    cleaned = []
    for order in orders:
        if not order["order_id"]:
            continue
        if not order["country"]:
            order["country"]="unknown"
        if not order["value"]:
            order["value"]=0
        cleaned.append(order)
    return cleaned

# Test
orders = [
    {"order_id": 1, "country": "DE", "value": 25.0, "status": "delivered"},
    {"order_id": 2, "country": None, "value": 15.0, "status": "delivered"},
    {"order_id": None, "country": "TR", "value": 30.0, "status": "pending"},  # removed
    {"order_id": 4, "country": "GR", "value": None, "status": None},
]
print(clean_orders(orders))
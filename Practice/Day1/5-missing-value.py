#Write a function that takes a list of orders and returns
# a new list where any order with a missing value is set to 0.
def clean_orders(orders):
    ss = []
    for order in orders:
        new = order.copy()
        if new.get("value") is None:
            new["value"] = 0
        ss.append(new)
    return ss
dirty_orders = [
    {"customer": "Alice", "value": 100},
    {"customer": "Bob"},
    {"customer": "Charlie", "value": None}
]
expected_cleaned = [
    {"customer": "Alice", "value": 100},
    {"customer": "Bob", "value": 0},
    {"customer": "Charlie", "value": 0}
]
assert clean_orders(dirty_orders) == expected_cleaned

# 5.2 All Valid
clean_already = [{"customer": "Alice", "value": 50}]
assert clean_orders(clean_already) == [{"customer": "Alice", "value": 50}]

# 5.3 Immutability Check (Making sure the original list wasn't modified)
original = [{"customer": "Alice"}]
result = clean_orders(original)
assert result == [{"customer": "Alice", "value": 0}]
assert original == [{"customer": "Alice"}], "Error: The original input list was mutated!"
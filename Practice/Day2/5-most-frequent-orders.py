#Given a list of orders, find the customer who placed
# the most orders (not highest value — most frequent).

def customer_with_most_orders(orders:list[dict])->str:
    counts = {}
    highest_num = 0
    highest_person = "No high person!"
    for order in orders:
        if order["customer_id"] in counts:
            counts[order["customer_id"]] += 1
        else:
            counts[order["customer_id"]] = 1
    for each in counts:
        if counts[each] > highest_num:
            highest_person = each
            highest_num = counts[each]

    return highest_person


test1 = [
    {"customer_id": "Alice"},
    {"customer_id": "Bob"},
    {"customer_id": "Alice"},
    {"customer_id": "Charlie"},
    {"customer_id": "Bob"},
    {"customer_id": "Bob"}
]
print(customer_with_most_orders(test1))
#the result: "Bob"

test2 = [
    {"customer_id": "Alice"}
]
print(customer_with_most_orders(test2))
#the result: "Alice"

test3 = []
print(customer_with_most_orders(test3))
#the result: None
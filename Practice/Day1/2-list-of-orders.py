#Write a function that takes a list of orders (each order is a dict with
# "customer" and "value") and returns the name of the customer who spent the most.

def most_val(orders:list[dict]):
    most_person = ""
    most_money = 0
    for order in orders:
        if order["value"] > most_money:
            most_person = order["customer"]
            most_money = order["value"]
    return most_person

test1 = [
    {"customer": "Alice", "value": 50},
    {"customer": "Bob", "value": 150},
    {"customer": "Charlie", "value": 75}
]
print(most_val(test1))

test2= [
    {"customer": "Alice", "value": 200},
    {"customer": "Bob", "value": 200}
]
print(most_val(test2))

test3= []
print(most_val(test3))
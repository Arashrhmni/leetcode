#Question 4 — Group Orders by Status
#Given a list of orders each with an order_id and status, return
# a dictionary where each status maps to a list of order IDs with that status.

def group_by_status(orders: list[dict])->dict:
    dict_of_result = {}
    for order in orders:
        if order["status"] not in dict_of_result:
            dict_of_result[order["status"]]=[order["order_id"]]
        else:
            dict_of_result[order["status"]].append(order["order_id"])
    return dict_of_result
        
# Test it
orders = [
    {"order_id": 1, "status": "delivered"},
    {"order_id": 2, "status": "pending"},
    {"order_id": 3, "status": "delivered"},
    {"order_id": 4, "status": "cancelled"},
    {"order_id": 5, "status": "pending"},
]
print(group_by_status(orders))
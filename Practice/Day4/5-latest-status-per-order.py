#Question 5 — Find the Latest Status per Order
#You have a list of log records, each with an order_id, timestamp, and status.
# For each order_id, return its most recent status.

def latest_status_per_order(logs: list[dict]) -> dict:
    most_recent = {}
    for log in logs:
        if log["order_id"] not in most_recent:
            most_recent[log["order_id"]]=log["timestamp"]
        else:
            if log["timestamp"]>most_recent[log["order_id"]]:
                most_recent[log["order_id"]]=log["timestamp"]
    for log in logs:
        if log["order_id"] in most_recent and log["timestamp"]== most_recent[log["order_id"]]:
            most_recent[log["order_id"]]=log["status"]
    return most_recent


# Test it
logs = [
    {"order_id": 1, "timestamp": "2024-01-01 10:00", "status": "created"},
    {"order_id": 1, "timestamp": "2024-01-01 10:15", "status": "preparing"},
    {"order_id": 1, "timestamp": "2024-01-01 10:45", "status": "delivered"},
    {"order_id": 2, "timestamp": "2024-01-01 11:00", "status": "created"},
    {"order_id": 2, "timestamp": "2024-01-01 11:20", "status": "cancelled"},
]
print(latest_status_per_order(logs))
# {1: "delivered", 2: "cancelled"}

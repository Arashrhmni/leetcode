
#Question 2 — Most Frequent Item
#Given a list of strings, return the one that appears
# most often. If there's a tie, return any of them.

def most_frequency(word: str)->dict:
    dictionary = {}
    num = 0
    most=""
    for letter in word:
        if letter in dictionary:
            dictionary[letter]+=1
        else:
            dictionary[letter]=1
    for each in dictionary:
        if dictionary[each]>num:
            most=each
            num = dictionary[each]
    return most
test1= "aassskfkrdkssdcef"
test2= "asdfgh"
test3= ""
print(most_frequency(test1))
print(most_frequency(test2))
print(most_frequency(test3))



print("-----------------")
#Question 3 — Theater Visibility (2D Matrix)
#You have rows of seats as a 2D list. Each number represents a person's
# height. A person can see the screen if they are taller than the person
# directly in front of them (the row before them). Row 0 is the front —
# everyone there can always see. Return True if everyone can see, False if anyone is blocked.

def theater_visibility(seats:list[list])->bool:
    for row_index in range(1, len(seats)): # start from row 1, row 0 always sees
        for col_index in range(len(seats[row_index])):
            current_person = seats[row_index][col_index]
            person_in_front = seats[row_index - 1][col_index]
            if current_person <= person_in_front:
                return False  # this person is blocked
    return True

test1 = [
    [1, 2, 3],  # Front row (always visible)
    [4, 5, 6],  # Everyone is taller than row 0
    [7, 8, 9]   # Everyone is taller than row 1
]
print(theater_visibility(test1)) #the result: True
test2 = [
    [2, 3, 2],
    [1, 5, 4],  # False because index 0 (height 1) cannot see over height 2
    [6, 7, 8]
]
print(theater_visibility(test2)) #the result: False
test3 = [
    [5, 5, 5]   # Single row - everyone can automatically see
]
print(theater_visibility(test3)) #the result: True



print("-----------------")
#Question 4 — Clean and Validate Orders
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




print("-----------------")
#Question 5 — Group Orders by Status
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




print("-----------------")
#Question 6 — Find the Latest Status per Order
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



print("-----------------")
#Question 7 — Find Duplicate Order IDs
#Given a list of order IDs where some may appear more
# than once, return a list of the ones that are duplicated.

def find_duplicates(orders:list)->list:
    all = []
    duplicates=[]
    for order in orders:
        if order in all:
            duplicates.append(order)
        else:
            all.append(order)
    return duplicates

# Test it
print(find_duplicates([1, 2, 3, 2, 4, 3, 5]))
# [2, 3]




print("-----------------")
#Question 8 — Null Percentage Quality Check
#Given a list of orders, calculate what percentage of records have a null value
# in each field. This is literally data quality scoring.

#I didn't do it :((
def quality_check(orders:list)->dict:
    total = len(orders)
    fields = orders[0].keys()
    result = {}
    for field in fields:
        null_count = sum(1 for order in orders if order.get(field) is None)
        result[field] = round((null_count / total) * 100, 2)
    
    return result


# Test it
orders = [
    {"order_id": 1, "country": "DE", "value": 25.0},
    {"order_id": 2, "country": None, "value": 15.0},
    {"order_id": 3, "country": "TR", "value": None},
    {"order_id": 4, "country": None, "value": None},
]
print(quality_check(orders))
# {"order_id": 0.0, "country": 50.0, "value": 50.0}



print("-----------------")
#Question 9 — Top N by Value
#Given a list of orders, return the top N orders by value. N is a parameter.

#I didn't do this one either :((
def top_n_orders(orders: list[dict], n: int) -> list[dict]:
    if n<=0:
        return False
    sorted_version = sorted(orders,key= lambda order:order["value"],reverse=True)
    return sorted_version[0:n]


# Test it
orders = [
    {"order_id": 1, "value": 25.0, "country": "DE"},
    {"order_id": 2, "value": 50.0, "country": "TR"},
    {"order_id": 3, "value": 10.0, "country": "GR"},
    {"order_id": 4, "value": 40.0, "country": "DE"},
    {"order_id": 5, "value": 30.0, "country": "TR"},
]
print(top_n_orders(orders, 3)) #expected: order 2 (50), order 4 (40), order 5 (30)




print("-----------------")
#Question 10 — String Compression
#Given a string, compress consecutive repeated characters into character+count
# format. If the compressed version isn't shorter, return the original.


def compress_string(text: str) -> str:
    if text == "":
        return ""
    all_letters=[]
    dict_of_all={}
    all_str=""
    for letter in text:
        if letter not in all_letters:
            all_letters.append(letter)
    for each in all_letters:
        for letter in text:
            if each == letter:
                if each in dict_of_all:
                    dict_of_all[each]+=1
                else:
                    dict_of_all[each]=1
    for key,value in dict_of_all.items():
        v=str(value)
        all_str+=key+v


    return all_str


# Test it
print(compress_string("aabcccdddd"))  # "a2b1c3d4"
print(compress_string("abc"))         # "abc" — compressed "a1b1c1" is longer
print(compress_string(""))            # ""
#Given two lists — one of customer IDs and one of orders each with
# a customer_id — return only the orders belonging to customers in the first list.

def belongin_to_first(customerIDs:list,orders:list[dict])->list:
    result = []
    for customerID in customerIDs:
        for order in orders:
            if customerID == order["customer_id"]:
                result.append(order)
    return result


test1_part1 = [1, 2, 3]
test1_part2 = [{"order_id": 101, "customer_id": 1}, {"order_id": 102, "customer_id": 4}, {"order_id": 103, "customer_id": 2}]
print(belongin_to_first(test1_part1,test1_part2))
#the result: [{"order_id": 101, "customer_id": 1}, {"order_id": 103, "customer_id": 2}]

test2_part1 = [99]
test2_part2 = [{"order_id": 201, "customer_id": 1}, {"order_id": 202, "customer_id": 2}]
print(belongin_to_first(test2_part1,test2_part2))
#the result: []

test3_part1 = []
test3_part2 = [{"order_id": 301, "customer_id": 1}]
print(belongin_to_first(test3_part1,test3_part2))
#the result: []
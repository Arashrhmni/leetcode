#Given a list of orders with "restaurant"
# and "value" fields, return the top 3 restaurants by total revenue.

def top3(restaurants:list[dict])->list:
    new_dict = {}
    top_restaurants = []
    for restaurant in restaurants:
        new_dict[restaurant["restaurant"]]=restaurant["value"]
    
    x = sorted(new_dict.values(), reverse=True)
    amount = 3
    for y in range(len(x)):
        if y < 3:
            for restaurant in restaurants:
                if x[y] == restaurant["value"]:
                    top_restaurants.append(restaurant["restaurant"])
                else:
                    continue
        else:
            break
    print(top_restaurants)
    return top_restaurants




#tests
test1 = [
    {"restaurant": "Pizza Hut", "value": 50},
    {"restaurant": "Burger King", "value": 30},
    {"restaurant": "Subway", "value": 40},
    {"restaurant": "McDonalds", "value": 100}
]
#the result: ["McDonalds", "Pizza Hut", "Subway"]

s = top3(test1)

test2 = [
    {"restaurant": "Taco Bell", "value": 10},
    {"restaurant": "KFC", "value": 15}
]
#the result: ["KFC", "Taco Bell"]
s = top3(test2)

test3 = []
#the result: []
s = top3(test3)
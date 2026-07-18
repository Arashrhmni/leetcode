#Given a list of orders, return the average order value
# per country, but only for countries with more than 2 orders.

def average_order_value(countries: list[dict])->dict:
    countries_count ={}
    countries_values ={}
    for country in countries:
        if country["country"] in countries_count:
            countries_count[country["country"]]+=1
        else:
            countries_count[country["country"]]=1
    for country in countries:
        if countries_count[country["country"]]>2:
            if country["country"] in countries_values:
                countries_values[country["country"]] = countries_values[country["country"]] + country["value"]
            else:
                countries_values[country["country"]] = country["value"]
    average = {}
    for each in countries_values:
        average[each]=countries_values[each]/countries_count[each]
    return average


test1 = [
    {"country": "USA", "value": 10},
    {"country": "USA", "value": 20},
    {"country": "USA", "value": 30},
    {"country": "Germany", "value": 50},
    {"country": "Germany", "value": 50},
    {"country": "France", "value": 100}
]
print(average_order_value(test1))
#the result: {"USA": 20.0}

test2 = [
    {"country": "UK", "value": 10},
    {"country": "UK", "value": 10},
    {"country": "UK", "value": 40},
    {"country": "Canada", "value": 20},
    {"country": "Canada", "value": 30},
    {"country": "Canada", "value": 40}
]
print(average_order_value(test2))
#the result: {"UK": 20.0, "Canada": 30.0}

test3 = [
    {"country": "Japan", "value": 100},
    {"country": "Japan", "value": 200}
]
print(average_order_value(test3))
#the result: {}
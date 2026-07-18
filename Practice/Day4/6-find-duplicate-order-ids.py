#Question 6 — Find Duplicate Order IDs
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
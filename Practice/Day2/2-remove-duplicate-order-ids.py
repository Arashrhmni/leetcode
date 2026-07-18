#Given a list of order IDs where some
# are duplicated, return a list with duplicates removed.
def duplicates_removed(orders:list)->list:
    sets = set(orders)
    main_list = list(sets)
    return main_list



test1 = [101, 102, 101, 103, 104, 102, 105]
print(duplicates_removed(test1))
#the result: [101, 102, 103, 104, 105]

test2 = [999, 999, 999]
print(duplicates_removed(test2))
#the result: [999]

test3 = []
print(duplicates_removed(test3))
#the result: []
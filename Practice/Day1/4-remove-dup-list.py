#Write a function that removes duplicate values from a list while keeping the original order.


def rem(values:list):
    if values:
        return set(values)
    else:
        return []

test1= [4, 5, 4, 1, 5, 2]
test2= ["a", "a", "a"]
test3= [1, "1", 1]
test4 = []
print(rem(test1))
print(rem(test2))
print(rem(test3))
print(rem(test4))
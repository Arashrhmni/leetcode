#Write a function that takes a list of strings and returns a
# dictionary where each string is a key and its length is the value.
def string_length(strings: list[str])->dict:
    d = {}
    for string in strings:
        d[string]=len(string)
    return d

test1 = ["apple", "banana", "cherry"]
print(string_length(test1))

test2 = ["", " ", "a"]
print(string_length(test2))

test3 = ["apple", "apple", "pear"]
print(string_length(test3))
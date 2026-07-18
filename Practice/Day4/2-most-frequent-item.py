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
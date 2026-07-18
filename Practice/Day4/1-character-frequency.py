#Question 1 — Character Frequency
#You have a string. Return a dictionary
# showing how many times each character appears.

def frequency(word: str)->dict:
    dictionary = {}
    for letter in word:
        if letter in dictionary:
            dictionary[letter]+=1
        else:
            dictionary[letter]=1
    return dictionary

test1= "aassskfkrdkssdcef"
test2= "asdfgh"
test3= ""
print(frequency(test1))
print(frequency(test2))
print(frequency(test3))
#Question 7 — String Compression
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
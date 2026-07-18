def even_nums(l: list[int]) -> list[int]:
    """
    Returns:
        list[int]: A list containing only the even numbers from the input list.
    """
    l2=[]
    for x in l:
        if x%2==0:
            l2.append(x)
    return l2


test1 = [1,2,3,4,5,6,7,8,9,10,11,12]
print(even_nums(test1))

test2 = [-2,-1,0,1,2,3,4]
print(even_nums(test2))

test3 = [1,3,5,7,9]
print(even_nums(test3))
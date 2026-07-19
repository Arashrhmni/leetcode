# 7. Reverse Integer
# https://leetcode.com/problems/reverse-integer/
# Difficulty: Medium
# Time: O(d) | Space: O(d)  — d = number of digits

class Solution:
    def reverse(self, x: int) -> int:
        is_less_than_0 = False
        if x >= 0:
            string_num = str(x)
        else:
            string_num = str(x)
            is_less_than_0 = True

        new_one = ""
        for letter in string_num[::-1]:
            new_one += letter
        if is_less_than_0:
            new_one = "-" + new_one[0:-1]
        last_number = int(new_one)
        if last_number > (-2)**31 and last_number < (2**31) - 1:
            return last_number
        else:
            return 0
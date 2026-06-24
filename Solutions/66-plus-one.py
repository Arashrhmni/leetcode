# 66. Plus One
# https://leetcode.com/problems/plus-one/
# Difficulty: Easy
# Time: O(n) | Space: O(n)

from typing import List

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        string = ""
        for x in digits:
            string += str(x)
        new = int(string)
        new += 1
        string1 = str(new)
        l = []
        for x in string1:
            l.append(int(x))
        return l
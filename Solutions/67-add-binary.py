# 67. Add Binary
# https://leetcode.com/problems/add-binary/
# Difficulty: Easy
# Time: O(n) | Space: O(n)

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        x = int(a, 2)
        y = int(b, 2)
        s = x + y
        s = bin(s)[2:]
        return s
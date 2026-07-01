# 13. Roman to Integer
# https://leetcode.com/problems/roman-to-integer/
# Difficulty: Easy
# Time: O(n) | Space: O(n)

class Solution:
    def romanToInt(self, s: str) -> int:
        dictionary = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        l = list(s)
        result = 0
        i = 0
        while i < len(l):
            if i + 1 < len(l) and l[i] == "I" and l[i+1] == "V":
                result += 4
                i += 2
            elif i + 1 < len(l) and l[i] == "I" and l[i+1] == "X":
                result += 9
                i += 2
            elif i + 1 < len(l) and l[i] == "X" and l[i+1] == "L":
                result += 40
                i += 2
            elif i + 1 < len(l) and l[i] == "X" and l[i+1] == "C":
                result += 90
                i += 2
            elif i + 1 < len(l) and l[i] == "C" and l[i+1] == "D":
                result += 400
                i += 2
            elif i + 1 < len(l) and l[i] == "C" and l[i+1] == "M":
                result += 900
                i += 2
            else:
                result += dictionary[l[i]]
                i += 1
        return result
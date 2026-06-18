# 3925. Concatenate Array With Reverse
# https://leetcode.com/problems/concatenate-array-with-reverse/
# Difficulty: Easy
# Time: O(n) | Space: O(n)

class Solution:
    def concatWithReverse(self, nums: list[int]) -> list[int]:
        l = nums.copy()
        l.reverse()
        s = nums + l
        return s
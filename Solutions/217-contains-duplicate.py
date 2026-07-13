# 217. Contains Duplicate
# https://leetcode.com/problems/contains-duplicate/
# Difficulty: Easy
# Time: O(n) | Space: O(n)

from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        l1 = set(nums)
        if len(l1) == len(nums):
            return False
        else:
            return True
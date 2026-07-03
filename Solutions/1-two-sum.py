# 1. Two Sum
# https://leetcode.com/problems/two-sum/
# Difficulty: Easy
# Time: O(n²) | Space: O(1)

from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i, j in enumerate(nums):
            for x, y in enumerate(nums):
                if x != i and j + y == target:
                    return [i, x]
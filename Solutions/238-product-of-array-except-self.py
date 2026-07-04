# 238. Product of Array Except Self
# https://leetcode.com/problems/product-of-array-except-self/
# Difficulty: Medium
# Time: O(n) | Space: O(1) — output array doesn't count

from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [1] * n
        prefix = 1
        for i in range(n):
            result[i] = prefix
            prefix *= nums[i]
        suffix = 1
        for i in range(n - 1, -1, -1):
            result[i] *= suffix
            suffix *= nums[i]

        return result
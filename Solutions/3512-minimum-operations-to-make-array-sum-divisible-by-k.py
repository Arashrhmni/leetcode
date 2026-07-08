# 3512. Minimum Operations to Make Array Sum Divisible by K
# https://leetcode.com/problems/minimum-operations-to-make-array-sum-divisible-by-k/
# Difficulty: Easy
# Time: O(n) | Space: O(1)

from typing import List

class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        return sum(nums) % k
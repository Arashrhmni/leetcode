# 35. Search Insert Position
# https://leetcode.com/problems/search-insert-position/
# Difficulty: Easy
# Time: O(n) | Space: O(1)
# Note: problem requires O(log n) — see binary search solution below

from typing import List

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        for x, y in enumerate(nums):
            if target == y:
                return x

        nums.append(target)
        nums = sorted(nums)
        return nums.index(target)
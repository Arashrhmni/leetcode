# 26. Remove Duplicates from Sorted Array
# https://leetcode.com/problems/remove-duplicates-from-sorted-array/
# Difficulty: Easy
# Time: O(n log n) | Space: O(n)

from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        sort = sorted(list(set(nums)))
        sort_size = len(sort)
        for i in range(sort_size):
            nums[i] = sort[i]
        return sort_size
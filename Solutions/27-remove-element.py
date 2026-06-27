# 27. Remove Element
# https://leetcode.com/problems/remove-element/
# Difficulty: Easy
# Time: O(n) | Space: O(n)

from typing import List

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        s = 0
        all_el = len(nums)
        list1 = nums.copy()
        for i in list1:
            if i == val:
                nums.remove(i)
                s += 1
        remaining = all_el - s
        return remaining
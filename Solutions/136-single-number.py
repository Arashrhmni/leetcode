# 136. Single Number
# https://leetcode.com/problems/single-number/
# Difficulty: Easy
# Time: O(n) | Space: O(n)

from typing import List

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        l = []
        for x in nums:
            if x in l:
                l.remove(x)
            else:
                l.append(x)
        return l[0]
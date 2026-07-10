# 3668. Restore Finishing Order
# https://leetcode.com/problems/restore-finishing-order/
# Difficulty: Easy
# Time: O(n) | Space: O(k)  — k = len(friends)

from typing import List

class Solution:
    def recoverOrder(self, order: List[int], friends: List[int]) -> List[int]:
        a = []
        for x in order:
            if x in friends:
                a.append(x)
        return a
# 3760. Maximum Substrings With Distinct Start
# https://leetcode.com/problems/maximum-substrings-with-distinct-start/
# Difficulty: Medium
# Time: O(n) | Space: O(n)

class Solution:
    def maxDistinct(self, s: str) -> int:
        return len(set(s))
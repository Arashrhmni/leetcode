# 14. Longest Common Prefix
# https://leetcode.com/problems/longest-common-prefix/
# Difficulty: Easy
# Time: O(n*m) | Space: O(n*m)

from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # Find the shortest word length
        min_len = min(len(s) for s in strs)

        # Create lists for each position
        lists = [[] for _ in range(min_len)]

        # Add each letter to its position's list
        for word in strs:
            for i in range(min_len):
                lists[i].append(word[i])

        # Check which positions have all matching letters
        res = ""
        for i in range(min_len):
            if len(set(lists[i])) == 1:  # All same
                res += lists[i][0]
            else:
                break

        return res
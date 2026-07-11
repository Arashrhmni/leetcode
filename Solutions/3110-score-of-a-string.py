# 3110. Score of a String
# https://leetcode.com/problems/score-of-a-string/
# Difficulty: Easy
# Time: O(n) | Space: O(1)

class Solution:
    def scoreOfString(self, s: str) -> int:
        t = 0
        for i in range(len(s) - 1):
            t += abs(ord(s[i]) - ord(s[i + 1]))
        return t
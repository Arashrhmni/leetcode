# 58. Length of Last Word
# https://leetcode.com/problems/length-of-last-word/
# Difficulty: Easy
# Time: O(n) | Space: O(n)

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        st = ""
        text = s
        g = True
        while g:
            if text[-1] != " ":
                g = False
            else:
                text = text[:-1]

        for x in text[::-1]:
            if x == " ":
                break
            else:
                st += x
        new = st[::-1]
        return len(new)
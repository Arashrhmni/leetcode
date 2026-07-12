# 2942. Find Words Containing Character
# https://leetcode.com/problems/find-words-containing-character/
# Difficulty: Easy
# Time: O(n*m) | Space: O(k)  — k = number of matching words

from typing import List

class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        a = []
        for i in range(len(words)):
            if x in words[i]:
                a.append(i)
        return a
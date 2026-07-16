# 3. Longest Substring Without Repeating Characters
# https://leetcode.com/problems/longest-substring-without-repeating-characters/
# Difficulty: Medium
# Time: O(n²) | Space: O(n)

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        substring_list = list(s)
        longest_num = 0
        if len(substring_list) == 1:
            return 1
        while substring_list:
            seen = {}
            for letter in substring_list:
                if letter in seen:
                    if len(seen) > longest_num:
                        longest_num = len(seen)
                    break
                else:
                    seen[letter] = True
            if len(seen) > longest_num:
                longest_num = len(seen)
            substring_list.pop(0)
        return longest_num
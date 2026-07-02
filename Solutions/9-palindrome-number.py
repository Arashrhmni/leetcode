# 9. Palindrome Number
# https://leetcode.com/problems/palindrome-number/
# Difficulty: Easy
# Time: O(n) | Space: O(n)

class Solution:
    def isPalindrome(self, x: int) -> bool:
        s = tuple(digit for digit in str(x))
        return s == s[::-1]
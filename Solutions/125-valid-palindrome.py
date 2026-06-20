# 125. Valid Palindrome
# https://leetcode.com/problems/valid-palindrome/
# Difficulty: Easy
# Time: O(n) | Space: O(n)

class Solution:
    def isPalindrome(self, s: str) -> bool:
        l = ["q","w","e","r","t","y","u","i","o","p","a","s","d","f","g","h","j","k","l",
             "z","x","c","v","b","n","m","1","2","3","4","5","6","7","8","9","0"]
        s = s.lower()
        string = ""
        for x in s:
            if x in l:
                string += x
        return string == string[::-1]
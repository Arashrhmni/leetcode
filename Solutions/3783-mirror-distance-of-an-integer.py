# 3783. Mirror Distance of an Integer
# https://leetcode.com/problems/mirror-distance-of-an-integer/
# Difficulty: Easy
# Time: O(d) | Space: O(d)  — d = number of digits

class Solution:
    def mirrorDistance(self, n: int) -> int:
        if n < 10:
            return 0
        j = reversed(str(n))
        s = ""
        for i in j:
            s = s + i
        k = int(s)
        if n - k < 0:
            return -(n - k)
        return n - k
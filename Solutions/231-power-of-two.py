# 231. Power of Two
# https://leetcode.com/problems/power-of-two/
# Difficulty: Easy
# Time: O(1) | Space: O(1)

import math

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n <= 0:
            return False
        elif math.log2(n).is_integer():
            return True
        else:
            return False
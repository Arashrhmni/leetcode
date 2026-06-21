# 88. Merge Sorted Array
# https://leetcode.com/problems/merge-sorted-array/
# Difficulty: Easy
# Time: O((m+n) log(m+n)) | Space: O(1)

from typing import List

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if m > 0:
            for x in range(len(nums1)):
                if m < len(nums1):
                    nums1.pop(m)
                else:
                    break
        else:
            nums1.clear()
        if n > 0:
            for x in range(len(nums2)):
                if n < len(nums2):
                    nums2.pop(n)
                else:
                    break
        else:
            nums2.clear()
        for y in nums2:
            nums1.append(y)
        nums1.sort()
#
# @lc app=leetcode id=4 lang=python3
#
# [4] Median of Two Sorted Arrays
#

# @lc code=start
from typing import List
from sys import maxsize


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        m, n = len(nums1), len(nums2)
        start, end = 0, m
        while True:
            i = (end + start) >> 1
            j = ((n + m + 1) >> 1) - i
            max_left_m = -maxsize if i == 0 else nums1[i-1]
            min_right_m = maxsize if i == m else nums1[i]
            max_left_n = -maxsize if j == 0 else nums2[j-1]
            min_right_n = maxsize if j == n else nums2[j]
            if max_left_m > min_right_n:
                end = i - 1
            elif max_left_n > min_right_m:
                start = i + 1
            else:
                return max(max_left_m, max_left_n) if (n + m) % 2 == 1 else (max(max_left_m, max_left_n) + min(min_right_m, min_right_n)) / 2
# @lc code=end

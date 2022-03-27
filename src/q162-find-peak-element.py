#
# @lc app=leetcode id=162 lang=python3
#
# [162] Find Peak Element
#
from re import M
from typing import List


# @lc code=start
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        nums.append(float('-inf'))
        i, j = 0, len(nums) - 2
        while i < j:
            middle = (i + j) >> 1
            if self.is_peak(i, nums):
                return i
            if self.is_peak(j, nums):
                return j
            if self.is_peak(middle, nums):
                return middle
            if self.is_increasing(middle, nums):
                i = middle + 1
            else:
                j = middle - 1
        return i

    def is_increasing(self, i, nums):
        return nums[i-1] < nums[i] < nums[i+1]

    def is_peak(self, i, nums):
        return nums[i-1] < nums[i] and nums[i] > nums[i+1]


# @lc code=end
solve = Solution().findPeakElement


def test_default():
    assert solve([1, 2, 3, 1]) == 2
    assert solve([1, 2, 1, 3, 5, 6, 4]) in {5, 1}


def test_corner_cases():
    assert solve([1]) == 0
    assert solve([-1]) == 0
    assert solve([-1, 1]) == 1
    assert solve([1, -1]) == 0
    assert solve([-2, 1, -1]) == 1
    assert solve([1, 0, -1]) == 0
    assert solve([-1, 0, 1]) == 2

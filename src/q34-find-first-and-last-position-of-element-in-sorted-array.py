#
# @lc app=leetcode id=34 lang=python3
#
# [34] Find First and Last Position of Element in Sorted Array
#
from typing import List

# @lc code=start


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1, -1]
        return [self.find_head(nums, 0, len(nums) - 1, target),
                self.find_tail(nums, 0, len(nums) - 1, target)]

    def find_head(self, nums, left, right, target):
        while left < right:
            middle = (left + right) >> 1
            if nums[middle] < target:
                left = middle + 1
            else:
                right = middle
        return left if nums[left] == target else -1

    def find_tail(self, nums, left, right, target):
        while left < right:
            middle = ((left + right) >> 1) + 1
            if nums[middle] > target:
                right = middle - 1
            else:
                left = middle
        return left if nums[left] == target else -1


# @lc code=end
solve = Solution().searchRange


def test_default():
    assert solve([5, 7, 7, 8, 8, 10], 8) == [3, 4]
    assert solve([5, 7, 7, 8, 8, 10], 6) == [-1, -1]


def test_corner_cases():
    assert solve([], 0) == [-1, -1]
    assert solve([0], 0) == [0, 0]
    assert solve([1], 0) == [-1, -1]
    assert solve([0, 0], 0) == [0, 1]

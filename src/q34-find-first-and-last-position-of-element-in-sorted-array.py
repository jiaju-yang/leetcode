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
        return [self.find_head(nums, target), self.find_tail(nums, target)]

    def find_head(self, nums, target):
        start, end = 0, len(nums) - 1
        while end >= start:
            middle = (end + start) >> 1
            if nums[middle] > target:
                end = middle - 1
            elif nums[middle] == target:
                if middle == 0 or nums[middle] != nums[middle - 1]:
                    return middle
                end = middle - 1
            else:
                start = middle + 1
        return -1

    def find_tail(self, nums, target):
        start, end = 0, len(nums) - 1
        while end >= start:
            middle = (end + start) >> 1
            if nums[middle] > target:
                end = middle - 1
            elif nums[middle] == target:
                if middle == len(nums) - 1 or nums[middle] != nums[middle + 1]:
                    return middle
                start = middle + 1
            else:
                start = middle + 1
        return -1


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

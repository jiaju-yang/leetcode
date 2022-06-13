#
# @lc app=leetcode id=35 lang=python3
#
# [35] Search Insert Position
#
from typing import List

# @lc code=start


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while left < right:
            middle = (left + right) >> 1
            if nums[middle] == target:
                return middle
            elif nums[middle] < target:
                left = middle + 1
            else:
                right = middle
        return left if nums[left] >= target else left + 1


# @lc code=end
solve = Solution().searchInsert


def test_default():
    assert solve([1, 3, 5, 6], 5) == 2
    assert solve([1, 3, 5, 6], 2) == 1
    assert solve([1, 3, 5, 6], 7) == 4


def test_corner_cases():
    assert solve([0], 1) == 1
    assert solve([-1], -2) == 0
    assert solve([-1, 1], -2) == 0
    assert solve([-1, 1], -1) == 0
    assert solve([-1, 1], 0) == 1
    assert solve([-1, 1], 1) == 1
    assert solve([-1, 1], 2) == 2

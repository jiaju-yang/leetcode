#
# @lc app=leetcode id=198 lang=python3
#
# [198] House Robber
#
from typing import List
# @lc code=start


class Solution:
    def rob(self, nums: List[int]) -> int:
        second_last, last = 0, nums[0]
        for i in range(1, len(nums)):
            second_last, last = last, max(last, second_last + nums[i])
        return last


# @lc code=end
solve = Solution().rob


def test_default():
    assert solve([1, 2, 3, 1]) == 4
    assert solve([2, 7, 9, 3, 1]) == 12


def test_corner_cases():
    assert solve([1]) == 1
    assert solve([2, 1]) == 2

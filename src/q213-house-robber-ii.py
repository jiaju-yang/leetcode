#
# @lc app=leetcode id=213 lang=python3
#
# [213] House Robber II
#
from typing import List
# @lc code=start


class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return self._rob(nums)
        return max(self._rob(nums[1:]), self._rob(nums[:-1]))

    def _rob(self, nums):
        second_last, last = 0, 0
        for num in nums:
            second_last, last = last, max(second_last + num, last)
        return last
# @lc code=end


solve = Solution().rob


def test_default():
    assert solve([2, 3, 2]) == 3
    assert solve([1, 2, 3, 1]) == 4
    assert solve([1, 2, 3]) == 3


def test_corners():
    assert solve([1]) == 1
    assert solve([1, 2]) == 2

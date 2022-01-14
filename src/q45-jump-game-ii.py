#
# @lc app=leetcode id=45 lang=python3
#
# [45] Jump Game II
#
from curses.ascii import SO
from sys import _current_frames
from typing import List


# @lc code=start
class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        jumps, cur_farest, next_farest = 1, nums[0], 0
        for i in range(1, len(nums)):
            if i > cur_farest:
                jumps, cur_farest = jumps + 1, next_farest
            next_farest = max(next_farest, i + nums[i])
        return jumps


# @lc code=end
solve = Solution().jump


def test_default():
    assert solve([2, 3, 1, 1, 4]) == 2
    assert solve([2, 3, 0, 1, 4]) == 2


def test_corner_cases():
    assert solve([1]) == 0
    assert solve([1, 0]) == 1
    assert solve([1, 2]) == 1
    assert solve([1, 1, 1, 1, 1]) == 4

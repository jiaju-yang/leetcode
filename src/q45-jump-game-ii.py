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
        jumps, cur_jump, next_jump = 0, 0, 0
        for i in range(len(nums) - 1):
            next_jump = max(next_jump, i + nums[i])
            if i == cur_jump:
                jumps += 1
                cur_jump = next_jump
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

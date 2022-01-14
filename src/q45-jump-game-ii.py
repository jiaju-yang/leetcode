#
# @lc app=leetcode id=45 lang=python3
#
# [45] Jump Game II
#
from curses.ascii import SO
from typing import List


# @lc code=start
class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        count = 1
        cur_start = 0
        cur_farest = nums[cur_start]
        while cur_farest < len(nums) - 1:
            count += 1
            next_start, next_farest = cur_start, cur_farest
            for i in range(cur_start + 1, cur_farest + 1):
                if i + nums[i] > next_farest:
                    next_start, next_farest = i, i + nums[i]
            cur_start, cur_farest = next_start, next_farest
        return count


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

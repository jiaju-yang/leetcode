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
        dp = [0] * len(nums)
        for i in range(1, len(nums)):
            cur_min = float('inf')
            for j in range(i):
                if j + nums[j] >= i and dp[j] + 1 < cur_min:
                    cur_min = dp[j] + 1
            dp[i] = cur_min
        return dp[-1]


# @lc code=end
solve = Solution().jump


def test_default():
    assert solve([2, 3, 1, 1, 4]) == 2
    assert solve([2, 3, 0, 1, 4]) == 2


def test_corner_cases():
    assert solve([1]) == 0
    assert solve([1, 0]) == 1
    assert solve([1, 2]) == 1

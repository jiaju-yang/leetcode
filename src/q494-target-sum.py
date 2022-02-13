#
# @lc app=leetcode id=494 lang=python3
#
# [494] Target Sum
#
from typing import List
from collections import defaultdict

# @lc code=start


class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        it = iter(nums)
        first = next(it)
        dp = defaultdict(int)
        dp[first] += 1
        dp[-first] += 1
        for num in it:
            new_dp = defaultdict(int)
            for k, v in dp.items():
                new_dp[k+num] += v
                new_dp[k-num] += v
            dp = new_dp
        return dp[target]


# @lc code=end
solve = Solution().findTargetSumWays


def test_default():
    assert solve([1, 1, 1, 1, 1], 3) == 5
    assert solve([43, 9, 26, 24, 39, 40, 20, 11, 18, 13, 14,
                 30, 48, 47, 37, 24, 32, 32, 2, 26], 47) == 5844


def test_corner_cases():
    assert solve([1], 1) == 1
    assert solve([1], 2) == 0
    assert solve([1], -1) == 1
    assert solve([1, 0], 1) == 2
    assert solve([0, 0, 0, 0, 0, 0, 0, 0, 1], 1) == 256

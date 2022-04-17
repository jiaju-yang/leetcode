#
# @lc app=leetcode id=377 lang=python3
#
# [377] Combination Sum IV
#
from typing import List

# @lc code=start


class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        dp = [0] * (target + 1)
        dp[0] = 1
        for i in range(1, target + 1):
            dp[i] = sum(dp[i-num] for num in nums if i - num >= 0)
        return dp[-1]

# @lc code=end


solve = Solution().combinationSum4


def test_default():
    assert solve([1, 2, 3], 4) == 7


def test_corner_cases():
    assert solve([9], 3) == 0
    assert solve([1], 1) == 1
    assert solve([1], 2) == 1

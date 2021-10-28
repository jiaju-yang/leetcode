#
# @lc app=leetcode id=322 lang=python3
#
# [322] Coin Change
#
from typing import List

# @lc code=start


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [-1] * (amount + 1)
        dp[0] = 0
        for i in range(amount):
            if dp[i] >= 0:
                for denomination in coins:
                    if i + denomination <= amount and (dp[i+denomination] == -1 or dp[i+denomination] > dp[i] + 1):
                        dp[i+denomination] = dp[i] + 1
        return dp[amount]
# @lc code=end


solve = Solution().coinChange


def test_default():
    assert solve([1, 2, 5], 11) == 3


def test_corner_cases():
    assert solve([1], 1) == 1
    assert solve([1], 0) == 0
    assert solve([1], 2) == 2
    assert solve([2], 1) == -1
    assert solve([2], 3) == -1

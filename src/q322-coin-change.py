#
# @lc app=leetcode id=322 lang=python3
#
# [322] Coin Change
#
from typing import List

# @lc code=start


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float("inf")] * (amount + 1)
        dp[0] = 0
        for i in range(1, amount + 1):
            for coin in coins:
                if i - coin >= 0 and dp[i-coin] < dp[i] - 1:
                    dp[i] = dp[i-coin] + 1
        return dp[amount] if dp[amount] != float("inf") else -1
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

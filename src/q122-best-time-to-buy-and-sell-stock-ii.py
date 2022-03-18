#
# @lc app=leetcode id=122 lang=python3
#
# [122] Best Time to Buy and Sell Stock II
#
from typing import List


# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        for i in range(len(prices)-1):
            profit += max(0, prices[i+1] - prices[i])
        return profit


# @lc code=end
solve = Solution().maxProfit


def test_default():
    assert solve([7, 1, 5, 3, 6, 4]) == 7
    assert solve([1, 2, 3, 4, 5]) == 4
    assert solve([7, 6, 4, 3, 1]) == 0


def test_corner_cases():
    assert solve([1]) == 0
    assert solve([0]) == 0
    assert solve([1, 2]) == 1
    assert solve([2, 1]) == 0
    assert solve([0, 0]) == 0
    assert solve([0, 1]) == 1

#
# @lc app=leetcode id=64 lang=python3
#
# [64] Minimum Path Sum
#
from typing import List

# @lc code=start


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        dp = [[float('inf')] * (n+1) for _ in range(m+1)]
        dp[1][0] = 0
        for i in range(1, m+1):
            for j in range(1, n+1):
                dp[i][j] = grid[i-1][j-1] + min(dp[i-1][j], dp[i][j-1])
        return dp[-1][-1]


# @lc code=end
solve = Solution().minPathSum


def test_default():
    assert solve([[1, 3, 1], [1, 5, 1], [4, 2, 1]]) == 7
    assert solve([[1, 2, 3], [4, 5, 6]]) == 12


def test_corner_cases():
    assert solve([[1]]) == 1
    assert solve([[1, 2]]) == 3
    assert solve([[1], [1]]) == 2

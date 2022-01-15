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
        dp = [[0] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if i == j == 0:
                    dp[i][j] = grid[i][j]
                else:
                    left_sum = dp[i-1][j] if i > 0 else float('inf')
                    up_sum = dp[i][j-1] if j > 0 else float('inf')
                    dp[i][j] = min(left_sum, up_sum) + grid[i][j]
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

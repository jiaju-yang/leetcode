#
# @lc app=leetcode id=62 lang=python3
#
# [62] Unique Paths
#


import math


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        dp[0][1] = 1
        for i in range(1, m+1):
            for j in range(1, n+1):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
        return dp[-1][-1]


# @lc code=start


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        if m == 1 or n == 1:
            return 1
        return math.factorial(m+n-2) // (math.factorial(m-1) * math.factorial(n-1))
# @lc code=end


solve = Solution().uniquePaths


def test_default():
    assert solve(3, 7) == 28
    assert solve(3, 2) == 3
    assert solve(3, 3) == 6


def test_corner_cases():
    assert solve(1, 1) == 1
    assert solve(1, 2) == 1
    assert solve(2, 1) == 1
    assert solve(2, 2) == 2

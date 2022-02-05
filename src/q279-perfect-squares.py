#
# @lc app=leetcode id=279 lang=python3
#
# [279] Perfect Squares
#

# @lc code=start
class Solution:
    def numSquares(self, n: int) -> int:
        squares = []
        i = 1
        while i*i <= n:
            squares.append(i*i)
            i += 1
        dp = [n] * (n+1)
        dp[0] = 0
        for i in range(1, n+1):
            for square in squares:
                if i - square >= 0:
                    dp[i] = min(dp[i-square] + 1, dp[i])
        return dp[n]


# @lc code=end
solve = Solution().numSquares


def test_default():
    assert solve(12) == 3
    assert solve(13) == 2


def test_corner_cases():
    assert solve(1) == 1
    assert solve(2) == 2
    assert solve(3) == 3
    assert solve(4) == 1

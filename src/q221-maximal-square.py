#
# @lc app=leetcode id=221 lang=python3
#
# [221] Maximal Square
#
from typing import List


# @lc code=start
class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        m, n = len(matrix), len(matrix[0])
        dp = [[0]*(n+1) for _ in range(m+1)]
        max_len = 0
        for i in range(1, m+1):
            for j in range(1, n+1):
                if matrix[i-1][j-1] == '1':
                    if dp[i-1][j] == dp[i][j-1]:
                        neighbour_max_len = dp[i-1][j]
                        if matrix[i-1-neighbour_max_len][j-1-neighbour_max_len] == '1':
                            dp[i][j] = neighbour_max_len + 1
                        else:
                            dp[i][j] = neighbour_max_len
                    else:
                        dp[i][j] = min(dp[i-1][j], dp[i][j-1])+1
                    max_len = max(dp[i][j], max_len)
        return max_len * max_len


# @lc code=end
solve = Solution().maximalSquare


def test_default():
    assert solve([['1', '0', '1', '0', '0'], ['1', '0', '1', '1', '1'], [
                 '1', '1', '1', '1', '1'], ['1', '0', '0', '1', '0']]) == 4


def test_corner_cases():
    assert solve([['0', '1'], ['1', '0']]) == 1
    assert solve([['1', '1'], ['1', '1']]) == 4
    assert solve([['1']]) == 1
    assert solve([['0']]) == 0

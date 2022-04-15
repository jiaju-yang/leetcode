#
# @lc app=leetcode id=1143 lang=python3
#
# [1143] Longest Common Subsequence
#

# @lc code=start
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m, n = len(text1), len(text2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        for i, c1 in enumerate(text1, start=1):
            for j, c2 in enumerate(text2, start=1):
                if c1 == c2:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        return dp[-1][-1]


# @lc code=end

solve = Solution().longestCommonSubsequence


def test_default():
    assert solve('ace', 'abcde') == 3
    assert solve('abcde', 'ace') == 3
    assert solve('abcde', 'aae') == 2
    assert solve('hofubmnylkra', 'pqhgxgdofcvmr') == 5
    assert solve('ezupkr', 'ubmrapg') == 2
    assert solve('oxcpqrsvwf', 'shmtulqrypy') == 2


def test_corner_cases():
    assert solve('', 'a') == 0
    assert solve('a', '') == 0
    assert solve('a', 'a') == 1
    assert solve('a', 'b') == 0
    assert solve('aa', 'b') == 0
    assert solve('aa', 'a') == 1
    assert solve('aa', 'aa') == 2

#
# @lc app=leetcode id=72 lang=python3
#
# [72] Edit Distance
#

# @lc code=start
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        if not word1:
            return len(word2)
        if not word2:
            return len(word1)
        dp = [[0] * (len(word2) + 1) for _ in range(len(word1) + 1)]
        for i in range(len(word2) + 1):
            dp[0][i] = i
        for i in range(len(word1) + 1):
            dp[i][0] = i
        for i in range(1, len(word1) + 1):
            for j in range(1, len(word2) + 1):
                if word1[i-1] == word2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = min(dp[i-1][j], dp[i-1][j-1], dp[i][j-1]) + 1
        return dp[-1][-1]


# @lc code=end
solve = Solution().minDistance


def test_default():
    assert solve('horse', 'ros') == 3
    assert solve('intention', 'execution') == 5


def test_corner_cases():
    assert solve('', '') == 0
    assert solve('', 'a') == 1
    assert solve('a', '') == 1
    assert solve('a', 'b') == 1
    assert solve('a', 'a') == 0
    assert solve('aa', 'a') == 1
    assert solve('ab', 'a') == 1
    assert solve('bb', 'a') == 2
    assert solve('a', 'aa') == 1
    assert solve('aa', 'aa') == 0
    assert solve('b', 'aa') == 2
    assert solve('a', 'bb') == 2
    assert solve('bb', 'aa') == 2

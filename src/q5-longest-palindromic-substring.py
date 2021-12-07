#
# @lc app=leetcode id=5 lang=python3
#
# [5] Longest Palindromic Substring
#

# @lc code=start
class Solution:
    def longestPalindrome(self, s: str) -> str:
        dp = [[False] * len(s) for _ in range(len(s))]
        start, end = 0, 0
        for i in range(len(s)):
            dp[i][i] = True
        for i in range(len(s)-2, -1, -1):
            for j in range(i+1, len(s)):
                if (j == i + 1 or dp[i+1][j-1]) and s[i] == s[j]:
                    dp[i][j] = True
                    if j - i > end - start:
                        start, end = i, j
        return s[start:end+1]


# @lc code=end
solve = Solution().longestPalindrome


def test_default():
    assert solve('babad') == 'bab' or 'aba'
    assert solve('cbbd') == 'bb'


def test_corner_cases():
    assert solve('a') == 'a'
    assert solve('ab') == 'a'
    assert solve('aba') == 'aba'

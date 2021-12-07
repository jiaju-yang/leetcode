#
# @lc app=leetcode id=5 lang=python3
#
# [5] Longest Palindromic Substring
#

# @lc code=start

class DPSolution:
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


class TwoPointersSolution:
    def longestPalindrome(self, s: str) -> str:
        start, end = 0, 0
        for i in range(len(s)):
            start, end = max((start, end),
                             self.extend(i, i, s),
                             self.extend(i, i+1, s),
                             key=lambda pair: pair[1] - pair[0])
        return s[start: end + 1]

    def extend(self, left, right, s):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return left+1, right-1


Solution = TwoPointersSolution

# @lc code=end
solve = Solution().longestPalindrome


def test_default():
    assert solve('babad') == 'bab' or 'aba'
    assert solve('cbbd') == 'bb'


def test_corner_cases():
    assert solve('a') == 'a'
    assert solve('ab') == 'a'
    assert solve('aba') == 'aba'

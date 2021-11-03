#
# @lc app=leetcode id=91 lang=python3
#
# [91] Decode Ways
#

# @lc code=start
class Solution:
    def numDecodings(self, s: str) -> int:
        dp = [0] * (len(s) + 1)
        dp[0] = 1
        for i in range(len(s)):
            if self.is_valid(s[i]):
                dp[i+1] += dp[i]
            if i > 0 and self.is_valid(s[i-1] + s[i]):
                dp[i+1] += dp[i-1]
        return dp[-1]

    def is_valid(self, t):
        if t.startswith('0'):
            return False
        return 1 <= int(t) <= 26
# @lc code=end


solve = Solution().numDecodings


def test_default():
    assert solve('11106') == 2
    assert solve('12') == 2
    assert solve('226') == 3


def test_corners():
    assert solve('0') == 0
    assert solve('06') == 0
    assert solve('6') == 1

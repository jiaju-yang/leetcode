#
# @lc app=leetcode id=32 lang=python3
#
# [32] Longest Valid Parentheses
#

# @lc code=start
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        longest = 0
        dp = [0] * len(s)
        for i, p in enumerate(s):
            if p == ')' and i > 0:
                prev_i = i - dp[i-1] - 1
                if prev_i >= 0 and s[prev_i] == '(':
                    dp[i] = dp[i-1] + 2 + \
                        (dp[i - dp[i-1] - 2] if i - dp[i-1] - 2 >= 0 else 0)
                    longest = max(longest, dp[i])
        return longest


# @lc code=end
solve = Solution().longestValidParentheses


def test_default():
    assert solve('(()') == 2
    assert solve(')()())') == 4
    assert solve(')(()))') == 4
    assert solve('()(()') == 2


def test_corner_cases():
    assert solve('') == 0
    assert solve('(') == 0
    assert solve(')') == 0
    assert solve('()') == 2

#
# @lc app=leetcode id=32 lang=python3
#
# [32] Longest Valid Parentheses
#
class DPSolution:
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


class StackSolution:
    def longestValidParentheses(self, s: str) -> int:
        stack = [(')', 0)]
        longest = 0
        for p in s:
            if p == '(':
                stack.append(('(', 0))
            else:
                prep_p, length = stack.pop()
                if prep_p == '(':
                    sec_last_p, prep_length = stack.pop()
                    if sec_last_p == '(':
                        stack.append(('(', 0))
                        stack.append((')', 2))
                    else:
                        stack.append((')', 2 + prep_length))
                elif length > 0:
                    if not stack:
                        stack.append((')', 0))
                    else:
                        sec_last_p, prep_length = stack.pop()
                        if sec_last_p == '(':
                            third_last_p, prep_prep_length = stack.pop()
                            if third_last_p == '(':
                                stack.append(('(', 0))
                            stack.append((')', prep_prep_length + 2 + length))
                        else:
                            stack.append((')', 0))
                else:
                    stack.append((')', 0))
                longest = max(longest, stack[-1][1])
        return longest

# @lc code=start


class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = [-1]
        longest = 0
        for i, p in enumerate(s):
            if p == '(':
                stack.append(i)
            else:
                stack.pop()
                if not stack:
                    stack.append(i)
                longest = max(longest, i-stack[-1])
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

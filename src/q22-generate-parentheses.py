#
# @lc app=leetcode id=22 lang=python3
#
# [22] Generate Parentheses
#
from typing import List

# @lc code=start


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        counter = {'(': n, ')': n}
        return self.dfs(counter)

    def dfs(self, counter):
        if counter['('] == 0 and counter[')'] == 0:
            return ['']
        if counter['('] == counter[')']:
            counter['('] -= 1
            result = ['(' + r for r in self.dfs(counter)]
            counter['('] += 1
            return result
        result = []
        if counter['('] > 0:
            counter['('] -= 1
            result.extend('(' + r for r in self.dfs(counter))
            counter['('] += 1
        if counter[')'] > 0:
            counter[')'] -= 1
            result.extend(')' + r for r in self.dfs(counter))
            counter[')'] += 1
        return result

# @lc code=end


solve = Solution().generateParenthesis


def test_default():
    assert set(solve(3)) == {"((()))", "(()())", "(())()", "()(())", "()()()"}


def test_corner_cases():
    assert solve(1) == ['()']

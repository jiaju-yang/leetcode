#
# @lc app=leetcode id=22 lang=python3
#
# [22] Generate Parentheses
#
from typing import List


class DFSSolution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        self.dfs(n, n, result, '')
        return result

    def dfs(self, left, right, result, cur):
        if left < 0 or right < 0 or left > right:
            return
        if left == right == 0:
            result.append(cur)
            return
        self.dfs(left-1, right, result, cur+'(')
        self.dfs(left, right-1, result, cur+')')
        return

# @lc code=start


class DPSolution:
    def generateParenthesis(self, n: int) -> List[str]:
        dp = [['']]
        for i in range(1, n+1):
            cur = []
            for j in range(i):
                for left in dp[j]:
                    for right in dp[i-j-1]:
                        cur.append(f'({left}){right}')
            dp.append(cur)
        return dp[-1]

# @lc code=end


solve = DPSolution().generateParenthesis


def test_default():
    assert set(solve(3)) == {"((()))", "(()())", "(())()", "()(())", "()()()"}


def test_corner_cases():
    assert solve(1) == ['()']

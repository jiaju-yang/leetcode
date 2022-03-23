#
# @lc app=leetcode id=150 lang=python3
#
# [150] Evaluate Reverse Polish Notation
#
from typing import List

# @lc code=start


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            try:
                stack.append(int(token))
            except ValueError:
                o1, o2 = stack.pop(), stack.pop()
                if token == '+':
                    stack.append(o1+o2)
                elif token == '-':
                    stack.append(o2-o1)
                elif token == '*':
                    stack.append(o1*o2)
                elif token == '/':
                    stack.append(int(o2/o1))
        return stack[0]


# @lc code=end
solve = Solution().evalRPN


def test_default():
    assert solve(['2', '1', '+', '3', '*']) == 9
    assert solve(['4', '13', '5', '/', '+']) == 6
    assert solve(['10', '6', '9', '3', '+', '-11', '*',
                 '/', '*', '17', '+', '5', '+']) == 22


def test_corner_cases():
    assert solve(['1']) == 1
    assert solve(['1', '2', '+']) == 3
    assert solve(['1', '2', '/']) == 0
    assert solve(['1', '2', '*']) == 2
    assert solve(['1', '2', '-']) == -1
    assert solve(['1', '-2', '+']) == -1
    assert solve(['1', '-2', '/']) == 0
    assert solve(['1', '-2', '*']) == -2
    assert solve(['1', '-2', '-']) == 3

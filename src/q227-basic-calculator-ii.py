#
# @lc app=leetcode id=227 lang=python3
#
# [227] Basic Calculator II
#
from operator import add, mul, sub
import re

# @lc code=start


class Solution:
    priorities = {
        '*': 2,
        '/': 2,
        '+': 1,
        '-': 1
    }
    operations = {
        '*': mul,
        '/': lambda a, b: int(a / b),
        '+': add,
        '-': sub
    }

    def calculate(self, s: str) -> int:
        s = s.replace(' ', '')
        s = re.split(r'(\+|-|\*|/)', s)
        numbers = []
        operators = []
        for c in s:
            if c in self.operations:
                if not operators:
                    operators.append(c)
                    continue
                while operators and self.priorities[c] <= self.priorities[operators[-1]]:
                    self.perform(numbers, operators)
                operators.append(c)
            else:
                try:
                    numbers.append(int(c))
                except ValueError:
                    pass
        while operators:
            self.perform(numbers, operators)
        return numbers[-1]

    def perform(self, numbers, operators):
        num1 = numbers.pop()
        num2 = numbers.pop()
        operator = operators.pop()
        numbers.append(self.operations[operator](num2, num1))


# @lc code=end
solve = Solution().calculate


def test_default():
    assert solve('3+2*2') == 7
    assert solve(' 3/2 ') == 1
    assert solve(' 3+5 / 2 ') == 5
    assert solve('1+1+1') == 3
    assert solve('1*2-3/4+5*6-7*8+9/10') == -24


def test_corner_cases():
    assert solve('1') == 1
    assert solve('0') == 0
    assert solve('0/1') == 0
    assert solve('0+0') == 0
    assert solve('0*10') == 0
    assert solve('0-10') == -10
    assert solve('1+1') == 2
    assert solve('3*2') == 6
    assert solve('3/2') == 1
    assert solve('3-2') == 1
    assert solve('1-2') == -1

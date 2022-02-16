#
# @lc app=leetcode id=739 lang=python3
#
# [739] Daily Temperatures
#
from typing import List

# @lc code=start


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        ret = [0] * len(temperatures)
        for i in range(len(temperatures)-1, -1, -1):
            tem = temperatures[i]
            while stack and stack[-1][0] <= tem:
                stack.pop()
            ret[i] = stack[-1][1] - i if stack else 0
            stack.append((tem, i))
        return ret


# @lc code=end
solve = Solution().dailyTemperatures


def test_default():
    assert solve([73, 74, 75, 71, 69, 72, 76, 73]) == [1, 1, 4, 2, 1, 1, 0, 0]
    assert solve([30, 40, 50, 60]) == [1, 1, 1, 0]
    assert solve([30, 60, 90]) == [1, 1, 0]


def test_corner_cases():
    assert solve([30]) == [0]
    assert solve([30, 31]) == [1, 0]
    assert solve([31, 30]) == [0, 0]
    assert solve([31, 31]) == [0, 0]

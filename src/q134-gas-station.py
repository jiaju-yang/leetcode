#
# @lc app=leetcode id=134 lang=python3
#
# [134] Gas Station
#
from typing import List

# @lc code=start


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        tank, total = 0, 0
        for i in range(len(gas)):
            if tank <= 0:
                start, tank = i, 0
            difference = gas[i] - cost[i]
            total += difference
            tank += difference
        return -1 if total < 0 else start


# @lc code=end

solve = Solution().canCompleteCircuit


def test_default():
    assert solve([1, 2, 3, 4, 5], [3, 4, 5, 1, 2]) == 3
    assert solve([2, 3, 4], [3, 4, 3]) == -1


def test_corner_cases():
    assert solve([1], [2]) == -1
    assert solve([1], [1]) == 0
    assert solve([1, 1], [2, 0]) == 1
    assert solve([1, 1], [0, 2]) == 0
    assert solve([1, 1], [2, 1]) == -1

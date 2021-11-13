#
# @lc app=leetcode id=57 lang=python3
#
# [57] Insert Interval
#
from typing import List

# @lc code=start


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        left, right = [], []
        for interval in intervals:
            if interval[1] < newInterval[0]:
                left.append(interval)
            elif interval[0] > newInterval[1]:
                right.append(interval)
            else:
                newInterval = [min(interval[0], newInterval[0]),
                               max(interval[1], newInterval[1])]
        return left + [newInterval] + right
# @lc code=end


solve = Solution().insert


def test_default():
    assert solve([[1, 3], [6, 9]], [2, 5]) == [[1, 5], [6, 9]]
    assert solve([[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]],
                 [4, 8]) == [[1, 2], [3, 10], [12, 16]]


def test_corner_cases():
    assert solve([], [5, 7]) == [[5, 7]]
    assert solve([[1, 5]], [2, 3]) == [[1, 5]]
    assert solve([[1, 5]], [2, 7]) == [[1, 7]]
    assert solve([[1, 5]], [0, 0]) == [[0, 0], [1, 5]]

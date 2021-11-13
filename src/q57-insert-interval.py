#
# @lc app=leetcode id=57 lang=python3
#
# [57] Insert Interval
#
from typing import List

# @lc code=start


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        result = []
        i = 0
        while i < len(intervals):
            if self.is_overlapping(intervals[i], newInterval) or newInterval[0] < intervals[i][0]:
                break
            result.append(list(intervals[i]))
            i += 1
        while i < len(intervals):
            if self.is_overlapping(intervals[i], newInterval):
                newInterval = self.merge_intervals(intervals[i], newInterval)
            else:
                break
            i += 1
        result.append(newInterval)
        while i < len(intervals):
            result.append(list(intervals[i]))
            i += 1
        return result

    def is_overlapping(self, interval_a, interval_b):
        return interval_a[0] <= interval_b[1] and interval_a[1] >= interval_b[0]

    def merge_intervals(self, interval_a, interval_b):
        return [min(interval_a[0], interval_b[0]), max(interval_a[1], interval_b[1])]
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

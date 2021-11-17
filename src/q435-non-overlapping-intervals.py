#
# @lc app=leetcode id=435 lang=python3
#
# [435] Non-overlapping Intervals
#
from typing import List
from operator import itemgetter

# @lc code=start


class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        result = []
        for interval in sorted(intervals, key=itemgetter(1)):
            if not result or result[-1][1] <= interval[0]:
                result.append(interval)
        return len(intervals) - len(result)


# @lc code=end
solve = Solution().eraseOverlapIntervals


def test_default():
    assert solve([[1, 2], [2, 3], [3, 4], [1, 3]]) == 1


def test_corner_cases():
    assert solve([[1, 2], [1, 2], [1, 2]]) == 2
    assert solve([[1, 2], [2, 3]]) == 0
    assert solve([]) == 0
    assert solve([[1, 2]]) == 0
    assert solve([[1, 5], [2, 3]]) == 1

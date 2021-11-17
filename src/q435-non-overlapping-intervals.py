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
        max_count, end_at = 0, float('-inf')
        for interval in sorted(intervals, key=itemgetter(1)):
            if end_at <= interval[0]:
                max_count += 1
                end_at = interval[1]
        return len(intervals) - max_count


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

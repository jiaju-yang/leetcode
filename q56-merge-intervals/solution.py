#
# @lc app=leetcode id=56 lang=python3
#
# [56] Merge Intervals
#

# @lc code=start
from typing import List
from operator import itemgetter


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []
        intervals.sort(key=itemgetter(0))
        result = [intervals[0]]
        for i in range(1, len(intervals)):
            if intervals[i][0] <= result[-1][1]:
                if result[-1][1] < intervals[i][1]:
                    result[-1][1] = intervals[i][1]
            else:
                result.append(intervals[i])
        return result

# @lc code=end

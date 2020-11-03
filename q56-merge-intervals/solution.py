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
        intervals.sort(key=itemgetter(0))
        result = []
        for interval in intervals:
            if result and interval[0] <= result[-1][1]:
                if result[-1][1] < interval[1]:
                    result[-1][1] = interval[1]
            else:
                result.append(interval)
        return result

# @lc code=end

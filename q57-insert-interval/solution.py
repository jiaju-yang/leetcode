#
# @lc app=leetcode id=57 lang=python3
#
# [57] Insert Interval
#

# @lc code=start
from typing import List


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        insert_location = 0
        while insert_location < len(intervals):
            if intervals[insert_location][0] < newInterval[0]:
                insert_location += 1
            else:
                break
        if insert_location > 0:
            previous = insert_location - 1
            if newInterval[0] <= intervals[previous][1]:
                newInterval[0] = intervals[previous][0]
                newInterval[1] = max(newInterval[1], intervals[previous][1])
                intervals.pop(previous)
                insert_location -= 1
        subsequent = insert_location
        while subsequent < len(intervals) and intervals[subsequent][0] <= newInterval[1]:
            newInterval[1] = max(newInterval[1], intervals[subsequent][1])
            intervals.pop(subsequent)
        intervals.insert(insert_location, newInterval)
        return intervals
# @lc code=end

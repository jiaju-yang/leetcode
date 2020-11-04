#
# @lc app=leetcode id=57 lang=python3
#
# [57] Insert Interval
#

# @lc code=start
from typing import List


class InPlaceSolution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        insert_location = 0
        while insert_location < len(intervals) and intervals[insert_location][0] < newInterval[0]:
            insert_location += 1
        previous = insert_location - 1
        if insert_location > 0 and newInterval[0] <= intervals[previous][1]:
            intervals[previous][1] = max(newInterval[1], intervals[previous][1])
            insert_location = previous
        else:
            intervals.insert(insert_location, newInterval)
        subsequent = insert_location + 1
        while subsequent < len(intervals) and intervals[subsequent][0] <= intervals[insert_location][1]:
            intervals[insert_location][1] = max(intervals[insert_location][1], intervals[subsequent][1])
            intervals.pop(subsequent)
        return intervals


class NoneInPlaceSolution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        left, right = [], []
        for interval in intervals:
            if interval[1] < newInterval[0]:
                left.append(interval)
            elif interval[0] > newInterval[1]:
                right.append(interval)
            else:
                newInterval[0] = min(interval[0], newInterval[0])
                newInterval[1] = max(interval[1], newInterval[1])
        left.append(newInterval)
        left.extend(right)
        return left

Solution = NoneInPlaceSolution
# @lc code=end

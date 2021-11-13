#
# @lc app=leetcode id=56 lang=python3
#
# [56] Merge Intervals
#
from typing import List
from operator import itemgetter

# @lc code=start


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []
        intervals.sort(key=itemgetter(0))
        it = iter(intervals)
        result = [next(it)]
        for interval in it:
            if interval[0] > result[-1][1]:
                result.append(interval)
            elif result[-1][1] < interval[1]:
                result[-1][1] = interval[1]
        return result


# @lc code=end

solve = Solution().merge


def test_default():
    assert solve([[1, 3], [2, 6], [8, 10], [15, 18]]) == [
        [1, 6], [8, 10], [15, 18]]
    assert solve([[1, 4], [4, 5]]) == [[1, 5]]


def test_corner_cases():
    assert solve([]) == []
    assert solve([[1, 2]]) == [[1, 2]]
    assert solve([[1, 2], [3, 4]]) == [[1, 2], [3, 4]]
    assert solve([[1, 2], [2, 4]]) == [[1, 4]]

#
# @lc app=leetcode id=986 lang=python3
#
# [986] Interval List Intersections
#

# @lc code=start
from typing import List


class Solution:
    def intervalIntersection(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        i, j = 0, 0
        result = []
        while i < len(A) and j < len(B):
            int_a, int_b = A[i], B[j]
            if int_a[1] >= int_b[0] and int_a[0] <= int_b[1]:
                result.append([max(int_a[0], int_b[0]),
                               min(int_a[1], int_b[1])])
            if int_a[1] < int_b[1]:
                i += 1
            else:
                j += 1
        return result
# @lc code=end

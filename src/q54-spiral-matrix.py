#
# @lc app=leetcode id=54 lang=python3
#
# [54] Spiral Matrix
#
from typing import List

# @lc code=start


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        return [] if not matrix else list(matrix[0]) + self.spiralOrder(list(zip(*matrix[1:]))[::-1])

# @lc code=end


solve = Solution().spiralOrder


def test_default():
    assert solve([[1, 2, 3], [4, 5, 6], [7, 8, 9]]) == [
        1, 2, 3, 6, 9, 8, 7, 4, 5]
    assert solve([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]) == [
        1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7]


def test_corner_cases():
    assert solve([[1]]) == [1]
    assert solve([[1, 2]]) == [1, 2]
    assert solve([[1], [2]]) == [1, 2]
    assert solve([[1, 2], [3, 4]]) == [1, 2, 4, 3]

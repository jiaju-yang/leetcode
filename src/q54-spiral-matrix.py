#
# @lc app=leetcode id=54 lang=python3
#
# [54] Spiral Matrix
#
from typing import List

# @lc code=start


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        row_start_at, row_end_at = 0, len(matrix) - 1
        col_start_at, col_end_at = 0, len(matrix[0]) - 1
        result = []
        while row_start_at < row_end_at and col_start_at < col_end_at:
            for col in range(col_start_at, col_end_at+1):
                result.append(matrix[row_start_at][col])
            for row in range(row_start_at + 1, row_end_at + 1):
                result.append(matrix[row][col_end_at])
            for col in range(col_end_at - 1, col_start_at - 1, -1):
                result.append(matrix[row_end_at][col])
            for row in range(row_end_at - 1, row_start_at, -1):
                result.append(matrix[row][col_start_at])
            row_start_at += 1
            row_end_at -= 1
            col_start_at += 1
            col_end_at -= 1
        if row_start_at == row_end_at and col_start_at < col_end_at:
            for col in range(col_start_at, col_end_at + 1):
                result.append(matrix[row_start_at][col])
        elif row_start_at < row_end_at and col_start_at == col_end_at:
            for row in range(row_start_at, row_end_at + 1):
                result.append(matrix[row][col_start_at])
        elif row_start_at == row_end_at and col_start_at == col_end_at:
            result.append(matrix[row_start_at][col_start_at])
        return result
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

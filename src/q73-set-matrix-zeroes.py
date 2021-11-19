#
# @lc app=leetcode id=73 lang=python3
#
# [73] Set Matrix Zeroes
#
from typing import List

# @lc code=start


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        zero_rows = set()
        zero_columns = set()
        r, c = len(matrix), len(matrix[0])
        for i in range(r):
            for j in range(c):
                if matrix[i][j] == 0:
                    zero_rows.add(i)
                    zero_columns.add(j)
        for i in range(r):
            for j in range(c):
                if i in zero_rows or j in zero_columns:
                    matrix[i][j] = 0

# @lc code=end


solve = Solution().setZeroes


def test_default():
    matrix = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
    solve(matrix)
    assert matrix == [[1, 0, 1], [0, 0, 0], [1, 0, 1]]

    matrix = [[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]]
    solve(matrix)
    assert matrix == [[0, 0, 0, 0], [0, 4, 5, 0], [0, 3, 1, 0]]


def test_corner_cases():
    matrix = [[1]]
    solve(matrix)
    assert matrix == [[1]]

    matrix = [[0]]
    solve(matrix)
    assert matrix == [[0]]

    matrix = [[0, 1]]
    solve(matrix)
    assert matrix == [[0, 0]]

    matrix = [[0], [1]]
    solve(matrix)
    assert matrix == [[0], [0]]

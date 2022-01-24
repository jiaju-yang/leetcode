#
# @lc app=leetcode id=74 lang=python3
#
# [74] Search a 2D Matrix
#
from typing import List

# @lc code=start


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row_i = self.which_row(matrix, target)
        return self.binary_search(matrix[row_i], target)

    def binary_search(self, row, target):
        left, right = 0, len(row) - 1
        while left <= right:
            middle = (left + right) >> 1
            if target == row[middle]:
                return True
            elif target < row[middle]:
                right = middle - 1
            else:
                left = middle + 1
        return False

    def which_row(self, matrix, target):
        m = len(matrix)
        left, right = 0, m-1
        while left <= right:
            middle = (left + right) >> 1
            if target >= matrix[right][0]:
                return right
            elif target < matrix[middle][0]:
                right = middle - 1
            elif right - left == 1:
                return left
            else:
                left = middle
        return middle


# @lc code=end
solve = Solution().searchMatrix


def test_default():
    assert solve([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 3)
    assert solve([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 11)
    assert not solve([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 13)


def test_corner_cases():
    assert solve([[1]], 1)
    assert not solve([[1]], 2)
    assert not solve([[1, 2]], 3)
    assert solve([[1, 2]], 1)
    assert solve([[1], [2]], 1)
    assert not solve([[1], [2]], 3)

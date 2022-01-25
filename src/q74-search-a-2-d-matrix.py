#
# @lc app=leetcode id=74 lang=python3
#
# [74] Search a 2D Matrix
#
from typing import List

# @lc code=start


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        left, right = 0, self.index(m-1, n-1, n)
        while left <= right:
            middle = (left + right) >> 1
            i, j = self.i_j(middle, n)
            if target == matrix[i][j]:
                return True
            elif target < matrix[i][j]:
                right = middle - 1
            else:
                left = middle + 1
        return False

    def index(self, i, j, n):
        return i * n + j

    def i_j(self, index, n):
        return index // n, index % n


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

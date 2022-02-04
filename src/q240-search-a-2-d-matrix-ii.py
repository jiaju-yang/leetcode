#
# @lc app=leetcode id=240 lang=python3
#
# [240] Search a 2D Matrix II
#
from typing import List

# @lc code=start


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        return self.searchInArea(matrix, (0, 0), (len(matrix) - 1, len(matrix[0]) - 1), target)

    def searchInArea(self, matrix, left_top, right_bottom, target):
        if left_top[0] > right_bottom[0] or left_top[1] > right_bottom[1]:
            return False
        if left_top == right_bottom:
            return matrix[left_top[0]][left_top[1]] == target
        middle_i = (left_top[0] + right_bottom[0]) >> 1
        middle_j = (left_top[1] + right_bottom[1]) >> 1
        if target == matrix[middle_i][middle_j]:
            return True
        elif target < matrix[middle_i][middle_j]:
            return self.searchInArea(matrix, left_top, (middle_i-1, right_bottom[1]), target) or \
                self.searchInArea(matrix, (middle_i, 0),
                                  (right_bottom[0], middle_j-1), target)
        else:
            return self.searchInArea(matrix, (middle_i+1, left_top[1]), right_bottom, target) or \
                self.searchInArea(
                    matrix, (left_top[0], middle_j+1), (middle_i, right_bottom[1]), target)


# @lc code=end
solve = Solution().searchMatrix


def test_default():
    assert solve([[1, 4, 7, 11, 15],
                  [2, 5, 8, 12, 19],
                  [3, 6, 9, 16, 22],
                  [10, 13, 14, 17, 24],
                  [18, 21, 23, 26, 30]], 5)
    assert not solve([[1, 4, 7, 11, 15],
                      [2, 5, 8, 12, 19],
                      [3, 6, 9, 16, 22],
                      [10, 13, 14, 17, 24],
                      [18, 21, 23, 26, 30]], 20)


def test_corner_cases():
    assert solve([[1]], 1)
    assert not solve([[1]], 2)
    assert solve([[1, 2], [3, 4]], 1)
    assert solve([[1, 2], [3, 4]], 2)
    assert solve([[1, 2], [3, 4]], 3)
    assert solve([[1, 2], [3, 4]], 4)
    assert not solve([[1, 2], [3, 4]], 5)

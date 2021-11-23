#
# @lc app=leetcode id=48 lang=python3
#
# [48] Rotate Image
#
from typing import List

# @lc code=start


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        matrix[:] = map(list, zip(*(matrix[::-1])))

# @lc code=end


solve = Solution().rotate


def test_default():
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    solve(matrix)
    assert matrix == [[7, 4, 1], [8, 5, 2], [9, 6, 3]]

    matrix = [[5, 1, 9, 11], [2, 4, 8, 10], [13, 3, 6, 7], [15, 14, 12, 16]]
    solve(matrix)
    assert matrix == [[15, 13, 2, 5], [14, 3, 4, 1],
                      [12, 6, 8, 9], [16, 7, 10, 11]]


def test_corner_cases():
    matrix = [[1]]
    solve(matrix)
    assert matrix == [[1]]

    matrix = [[1, 2], [3, 4]]
    solve(matrix)
    assert matrix == [[3, 1], [4, 2]]

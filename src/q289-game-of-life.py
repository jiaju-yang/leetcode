#
# @lc app=leetcode id=289 lang=python3
#
# [289] Game of Life
#
from typing import List

# @lc code=start


class Solution:
    adjs = (
        (-1, 0), (1, 0), (0, -1), (0, 1),
        (1, 1), (1, -1), (-1, 1), (-1, -1)
    )

    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m, n = len(board), len(board[0])
        new_board = [[0] * n for i in range(m)]
        for i in range(m):
            for j in range(n):
                count = 0
                for offset_x, offset_y in self.adjs:
                    adj_i, adj_j = i + offset_x, j + offset_y
                    if 0 <= adj_i < m and 0 <= adj_j < n:
                        count += board[adj_i][adj_j]
                if count < 2:
                    new_board[i][j] = 0
                elif count > 3:
                    new_board[i][j] = 0
                elif count == 3:
                    new_board[i][j] = 1
                else:
                    new_board[i][j] = board[i][j]
        board[:] = new_board[:]


# @lc code=end
solve = Solution().gameOfLife


def test_default():
    board = [[0, 1, 0], [0, 0, 1], [1, 1, 1], [0, 0, 0]]
    solve(board)
    assert board == [[0, 0, 0], [1, 0, 1], [0, 1, 1], [0, 1, 0]]

    board = [[1, 1], [1, 0]]
    solve(board)
    assert board == [[1, 1], [1, 1]]


def test_corner_cases():
    board = [[1]]
    solve(board)
    assert board == [[0]]

    board = [[0]]
    solve(board)
    assert board == [[0]]

    board = [[0, 1], [1, 0]]
    solve(board)
    assert board == [[0, 0], [0, 0]]

    board = [[1, 1], [1, 1]]
    solve(board)
    assert board == [[1, 1], [1, 1]]

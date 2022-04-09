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
        for i in range(m):
            for j in range(n):
                count = 0
                for offset_x, offset_y in self.adjs:
                    adj_i, adj_j = i + offset_x, j + offset_y
                    if 0 <= adj_i < m and 0 <= adj_j < n:
                        count += board[adj_i][adj_j] % 2
                if count == 3 and board[i][j] == 0:
                    board[i][j] = 2
                elif board[i][j] == 1 and (count < 2 or count > 3):
                    board[i][j] = 3
        for i in range(m):
            for j in range(n):
                if board[i][j] == 2:
                    board[i][j] = 1
                elif board[i][j] == 3:
                    board[i][j] = 0


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

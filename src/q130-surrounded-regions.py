#
# @lc app=leetcode id=130 lang=python3
#
# [130] Surrounded Regions
#
from typing import List

# @lc code=start


class Solution:
    adjs = ((0, 1), (1, 0), (-1, 0), (0, -1))

    def solve(self, board: List[List[str]]) -> None:
        '''
        Do not return anything, modify board in-place instead.
        '''
        m, n = len(board), len(board[0])
        for i in range(n):
            self.dfs(board, 0, i, m, n)
            self.dfs(board, m - 1, i, m, n)
        for i in range(m):
            self.dfs(board, i, 0, m, n)
            self.dfs(board, i, n - 1, m, n)
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'N':
                    board[i][j] = 'O'
                elif board[i][j] == 'O':
                    board[i][j] = 'X'

    def dfs(self, board, i, j, m, n):
        if board[i][j] != 'O':
            return
        board[i][j] = 'N'
        for offset_x, offset_y in self.adjs:
            adj_i, adj_j = offset_x + i, offset_y + j
            if 0 <= adj_i < m and 0 <= adj_j < n:
                self.dfs(board, adj_i, adj_j, m, n)


# @lc code=end
solve = Solution().solve


def test_default():
    board = [['X', 'X', 'X', 'X'], ['X', 'O', 'O', 'X'],
             ['X', 'X', 'O', 'X'], ['X', 'O', 'X', 'X']]
    solve(board)
    assert board == [['X', 'X', 'X', 'X'], ['X', 'X', 'X', 'X'], [
        'X', 'X', 'X', 'X'], ['X', 'O', 'X', 'X']]

    board = [['X', 'O', 'X', 'O', 'X', 'O'],
             ['O', 'X', 'O', 'X', 'O', 'X'],
             ['X', 'O', 'X', 'O', 'X', 'O'],
             ['O', 'X', 'O', 'X', 'O', 'X']]
    solve(board)
    assert board == [['X', 'O', 'X', 'O', 'X', 'O'],
                     ['O', 'X', 'X', 'X', 'X', 'X'],
                     ['X', 'X', 'X', 'X', 'X', 'O'],
                     ['O', 'X', 'O', 'X', 'O', 'X']]


def test_corner_cases():
    board = [['X']]
    solve(board)
    assert board == [['X']]

    board = [['O']]
    solve(board)
    assert board == [['O']]

    board = [['O', 'O'], ['O', 'O']]
    solve(board)
    assert board == [['O', 'O'], ['O', 'O']]

    board = [['X', 'X'], ['X', 'X']]
    solve(board)
    assert board == [['X', 'X'], ['X', 'X']]

    board = [['X', 'X', 'X'], ['X', 'O', 'X'], ['X', 'X', 'X']]
    solve(board)
    assert board == [['X', 'X', 'X'], ['X', 'X', 'X'], ['X', 'X', 'X']]

    board = [['X', 'X', 'X'], ['X', 'X', 'X'], ['X', 'X', 'X']]
    solve(board)
    assert board == [['X', 'X', 'X'], ['X', 'X', 'X'], ['X', 'X', 'X']]

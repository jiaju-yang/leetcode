#
# @lc app=leetcode id=79 lang=python3
#
# [79] Word Search
#
from typing import List

# @lc code=start


class Solution:
    adjacents = ((0, 1), (1, 0), (-1, 0), (0, -1))

    def exist(self, board: List[List[str]], word: str) -> bool:
        for row in range(len(board)):
            for col in range(len(board[0])):
                if board[row][col] == word[0]:
                    result = self.dfs(board, word, row, col)
                    if result:
                        return True
        return False

    def dfs(self, board, remain, row, col):
        if len(remain) == 1:
            return True
        char = remain[0]
        new_remain = remain[1:]
        board[row][col] = True
        for row_off, col_off in self.adjacents:
            adj_row, adj_col = row_off + row, col_off + col
            if 0 <= adj_row < len(board) and 0 <= adj_col < len(board[0]) and board[adj_row][adj_col] is not True and board[adj_row][adj_col] == new_remain[0]:
                result = self.dfs(board, new_remain, adj_row, adj_col)
                if result:
                    return True
        board[row][col] = char
        return False

# @lc code=end


solve = Solution().exist


def test_default():
    assert solve([['A', 'B', 'C', 'E'], ['S', 'F', 'C', 'S'],
                 ['A', 'D', 'E', 'E']], 'ABCCED')
    assert solve([['A', 'B', 'C', 'E'], ['S', 'F', 'C', 'S'],
                 ['A', 'D', 'E', 'E']], 'SEE')
    assert not solve([['A', 'B', 'C', 'E'], ['S', 'F', 'C', 'S'],
                      ['A', 'D', 'E', 'E']], 'ABCB')


def test_corner_cases():
    assert solve([['A']], 'A')
    assert solve([['A', 'B']], 'AB')
    assert solve([['A', 'B']], 'BA')
    assert not solve([['A']], 'BA')
    assert not solve([['A']], 'AB')
    assert not solve([['A', 'B']], 'AC')

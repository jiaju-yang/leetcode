#
# @lc app=leetcode id=36 lang=python3
#
# [36] Valid Sudoku
#
from typing import Counter, List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in board:
            if not self.are_digits_valid(*row):
                return False
        for col in zip(*board):
            if not self.are_digits_valid(*col):
                return False
        for start_i in range(0, len(board), 3):
            for start_j in range(0, len(board[0]), 3):
                if not self.are_digits_valid(*(board[i][j] for j in range(start_j, start_j + 3)
                                               for i in range(start_i, start_i + 3))):
                    return False

        return True

    def are_digits_valid(self, *digits):
        counter = Counter(digits)
        return all(count <= 1 for key, count in counter.items() if key != '.')

# @lc code=start


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        seen = set()
        for i, row in enumerate(board):
            for j, c in enumerate(row):
                if c != '.':
                    if (i, c) in seen or (c, j) in seen or (i//3, j//3, c) in seen:
                        return False
                    seen.add((i, c))
                    seen.add((c, j))
                    seen.add((i//3, j//3, c))
        return True

# @lc code=end


solve = Solution().isValidSudoku


def test_default():
    assert solve([['5', '3', '.', '.', '7', '.', '.', '.', '.'], ['6', '.', '.', '1', '9', '5', '.', '.', '.'], ['.', '9', '8', '.', '.', '.', '.', '6', '.'], ['8', '.', '.', '.', '6', '.', '.', '.', '3'], [
                 '4', '.', '.', '8', '.', '3', '.', '.', '1'], ['7', '.', '.', '.', '2', '.', '.', '.', '6'], ['.', '6', '.', '.', '.', '.', '2', '8', '.'], ['.', '.', '.', '4', '1', '9', '.', '.', '5'], ['.', '.', '.', '.', '8', '.', '.', '7', '9']])
    assert not solve([['8', '3', '.', '.', '7', '.', '.', '.', '.'], ['6', '.', '.', '1', '9', '5', '.', '.', '.'], ['.', '9', '8', '.', '.', '.', '.', '6', '.'], ['8', '.', '.', '.', '6', '.', '.', '.', '3'], [
        '4', '.', '.', '8', '.', '3', '.', '.', '1'], ['7', '.', '.', '.', '2', '.', '.', '.', '6'], ['.', '6', '.', '.', '.', '.', '2', '8', '.'], ['.', '.', '.', '4', '1', '9', '.', '.', '5'], ['.', '.', '.', '.', '8', '.', '.', '7', '9']])


def test_corner_cases():
    assert solve([['.', '.', '.', '.', '.', '.', '.', '.', '.'], ['.', '.', '.', '.', '.', '.', '.', '.', '.'], ['.', '.', '.', '.', '.', '.', '.', '.', '.'], ['.', '.', '.', '.', '.', '.', '.', '.', '.'], [
                 '.', '.', '.', '.', '.', '.', '.', '.', '.'], ['.', '.', '.', '.', '.', '.', '.', '.', '.'], ['.', '.', '.', '.', '.', '.', '.', '.', '.'], ['.', '.', '.', '.', '.', '.', '.', '.', '.'], ['.', '.', '.', '.', '.', '.', '.', '.', '.']])

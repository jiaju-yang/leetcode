#
# @lc app=leetcode id=212 lang=python3
#
# [212] Word Search II
#
from typing import List
from collections import defaultdict


# @lc code=start
class Solution:
    adjs = ((-1, 0), (1, 0), (0, -1), (0, 1))

    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        result = []
        for word in words:
            if self.is_word_in(board, word):
                result.append(word)
        return result

    def is_word_in(self, board, word):
        m, n = len(board), len(board[0])
        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0] and self.dfs(board, i, j, word):
                    return True

    def dfs(self, matrix, start_i, start_j, remain):
        if len(remain) == 1:
            return True
        m, n = len(matrix), len(matrix[0])
        matrix[start_i][start_j] = True
        match, remain = remain[0], remain[1:]
        for x, y in self.adjs:
            next_i, next_j = start_i + x, start_j + y
            if 0 <= next_i < m and 0 <= next_j < n and matrix[next_i][next_j] == remain[0]:
                if self.dfs(matrix, next_i, next_j, remain):
                    matrix[start_i][start_j] = match
                    return True
        matrix[start_i][start_j] = match
        return False


# @lc code=end
solve = Solution().findWords


def test_default():
    assert solve([['o', 'a', 'a', 'n'], ['e', 't', 'a', 'e'], ['i', 'h', 'k', 'r'], [
                 'i', 'f', 'l', 'v']], ['oath', 'pea', 'eat', 'rain']) == ['oath', 'eat']
    assert solve([['a', 'b'], ['c', 'd']], ['abcb']) == []


def test_corner_cases():
    assert solve([['a']], ['a']) == ['a']
    assert solve([['a']], ['b']) == []
    assert solve([['a'], ['b']], ['ab', 'ba']) == ['ab', 'ba']

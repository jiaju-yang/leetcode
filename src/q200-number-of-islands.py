#
# @lc app=leetcode id=200 lang=python3
#
# [200] Number of Islands
#
from typing import List


# @lc code=start
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        row = len(grid)
        column = len(grid[0])
        states = [[False] * column for _ in range(row)]
        adjacents = ((0, 1), (1, 0), (-1, 0), (0, -1))

        def dfs(i, j):
            states[i][j] = True
            for i_off, j_off in adjacents:
                neighbor_i, neighbor_j = i + i_off, j + j_off
                if 0 <= neighbor_i < row and 0 <= neighbor_j < column and grid[neighbor_i][neighbor_j] == '1' and not states[neighbor_i][neighbor_j]:
                    dfs(neighbor_i, neighbor_j)

        num_of_islands = 0
        for i in range(row):
            for j in range(column):
                if not states[i][j] and grid[i][j] == '1':
                    num_of_islands += 1
                    dfs(i, j)

        return num_of_islands


# @lc code=end
solve = Solution().numIslands


def test_default():
    assert solve([
        ['1', '1', '1', '1', '0'],
        ['1', '1', '0', '1', '0'],
        ['1', '1', '0', '0', '0'],
        ['0', '0', '0', '0', '0']
    ]) == 1
    assert solve([
        ['1', '1', '0', '0', '0'],
        ['1', '1', '0', '0', '0'],
        ['0', '0', '1', '0', '0'],
        ['0', '0', '0', '1', '1']
    ]) == 3


def test_corner_cases():
    assert solve([['1']]) == 1
    assert solve([['0']]) == 0
    assert solve([['0', '1'], ['1', '0']]) == 2

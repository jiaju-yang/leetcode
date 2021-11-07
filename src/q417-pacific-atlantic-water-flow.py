#
# @lc app=leetcode id=417 lang=python3
#
# [417] Pacific Atlantic Water Flow
#
from typing import List

# @lc code=start


class Solution:
    directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]

    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m = len(heights)
        n = len(heights[0])

        pacific_ocean_access = [[False] * n for _ in range(m)]
        for i in range(n):
            self.dfs((0, i), pacific_ocean_access, heights, m, n)
        for i in range(m):
            self.dfs((i, 0), pacific_ocean_access, heights, m, n)

        atlantic_ocean_access = [[False] * n for _ in range(m)]
        for i in range(n):
            self.dfs((m-1, i), atlantic_ocean_access, heights, m, n)
        for i in range(m):
            self.dfs((i, n-1), atlantic_ocean_access, heights, m, n)

        result = []
        for i in range(m):
            for j in range(n):
                if pacific_ocean_access[i][j] and atlantic_ocean_access[i][j]:
                    result.append([i, j])
        return result

    def dfs(self, node, states, heights, m, n):
        if states[node[0]][node[1]]:
            return
        states[node[0]][node[1]] = True
        for i, j in self.neighbors(node[0], node[1], heights, m, n):
            self.dfs((i, j), states, heights, m, n)

    def neighbors(self, i, j, heights, m, n):
        for neighbor_i_off, neighbor_j_off in self.directions:
            neighbor_i, neighbor_j = i + neighbor_i_off, j + neighbor_j_off
            if 0 <= neighbor_i < m and 0 <= neighbor_j < n and heights[i][j] <= heights[neighbor_i][neighbor_j]:
                yield (neighbor_i, neighbor_j)


# @lc code=end

solve = Solution().pacificAtlantic


def test_default():
    assert solve([[1, 2, 2, 3, 5], [3, 2, 3, 4, 4], [2, 4, 5, 3, 1], [6, 7, 1, 4, 5], [
                 5, 1, 1, 2, 4]]) == [[0, 4], [1, 3], [1, 4], [2, 2], [3, 0], [3, 1], [4, 0]]


def test_corner_cases():
    assert solve([[1]]) == [[0, 0]]
    assert solve([[2, 1], [1, 2]]) == [[0, 0], [0, 1], [1, 0], [1, 1]]

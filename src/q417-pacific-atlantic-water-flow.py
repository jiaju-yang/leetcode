#
# @lc app=leetcode id=417 lang=python3
#
# [417] Pacific Atlantic Water Flow
#
from typing import List
from collections import defaultdict

# @lc code=start


class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        adjs = defaultdict(list)
        m = len(heights)
        n = len(heights[0])
        neighbors = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        for i in range(m):
            for j in range(n):
                for neighbor_i_off, neighbor_j_off in neighbors:
                    neighbor_i, neighbor_j = i + neighbor_i_off, j + neighbor_j_off
                    if 0 <= neighbor_i < m and 0 <= neighbor_j < n and heights[i][j] <= heights[neighbor_i][neighbor_j]:
                        adjs[(i, j)].append((neighbor_i, neighbor_j))

        pacific_ocean_access = [[False] * n for _ in range(m)]
        for i in range(n):
            pacific_ocean_access[0][i] = True
        for i in range(m):
            pacific_ocean_access[i][0] = True
        for i in range(n):
            self.dfs((0, i), pacific_ocean_access, adjs)
        for i in range(m):
            self.dfs((i, 0), pacific_ocean_access, adjs)

        atlantic_ocean_access = [[False] * n for _ in range(m)]
        for i in range(n):
            atlantic_ocean_access[-1][i] = True
        for i in range(m):
            atlantic_ocean_access[i][-1] = True
        for i in range(n):
            self.dfs((m-1, i), atlantic_ocean_access, adjs)
        for i in range(m):
            self.dfs((i, n-1), atlantic_ocean_access, adjs)

        result = []
        for i in range(m):
            for j in range(n):
                if pacific_ocean_access[i][j] and atlantic_ocean_access[i][j]:
                    result.append([i, j])
        return result

    def dfs(self, node, states, adjs):
        states[node[0]][node[1]] = True
        for adj in adjs[node]:
            if not states[adj[0]][adj[1]]:
                self.dfs(adj, states, adjs)


# @lc code=end


solve = Solution().pacificAtlantic


def test_default():
    assert solve([[1, 2, 2, 3, 5], [3, 2, 3, 4, 4], [2, 4, 5, 3, 1], [6, 7, 1, 4, 5], [
                 5, 1, 1, 2, 4]]) == [[0, 4], [1, 3], [1, 4], [2, 2], [3, 0], [3, 1], [4, 0]]


def test_corner_cases():
    assert solve([[1]]) == [[0, 0]]
    assert solve([[2, 1], [1, 2]]) == [[0, 0], [0, 1], [1, 0], [1, 1]]

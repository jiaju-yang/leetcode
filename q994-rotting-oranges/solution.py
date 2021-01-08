#
# @lc app=leetcode id=994 lang=python3
#
# [994] Rotting Oranges
#

# @lc code=start
from typing import List
from collections import namedtuple


class Node:
    def __init__(self, position, state, adjs=None):
        if not adjs:
            adjs = []
        self.position = position
        self.state = state
        self.adjs = adjs


Position = namedtuple('Position', 'i, j')
directions = ((0, 1), (1, 0), (-1, 0), (0, -1))
EMPTY = 0
FRESH = 1
ROTTEN = 2


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        graph = {}
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                state = grid[i][j]
                if state != EMPTY:
                    position = Position(i, j)
                    node = Node(position, state)
                    for direction in directions:
                        adj_i, adj_j = i+direction[0], j+direction[1]
                        if len(grid) > adj_i >= 0 and len(grid[i]) > adj_j >= 0:
                            if grid[adj_i][adj_j] != EMPTY:
                                node.adjs.append(Position(adj_i, adj_j))
                    graph[position] = node

        minute = 0
        unresolved_rottened_pos = [
            node.position for node in graph.values() if node.state == ROTTEN]
        rottened_count = len(unresolved_rottened_pos)
        while unresolved_rottened_pos:
            fresh_adjs = set()
            for rottened_pos in unresolved_rottened_pos:
                rottened = graph[rottened_pos]
                for adj_position in rottened.adjs:
                    org = graph[adj_position]
                    if org.state == FRESH:
                        fresh_adjs.add(org.position)
            if len(fresh_adjs) > 0:
                minute += 1
            for adj in fresh_adjs:
                org = graph[adj]
                org.state = ROTTEN
                rottened_count += 1
            unresolved_rottened_pos = fresh_adjs
        return minute if rottened_count == len(graph) else -1

# @lc code=end

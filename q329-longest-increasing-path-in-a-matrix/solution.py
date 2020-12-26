#
# @lc app=leetcode id=329 lang=python3
#
# [329] Longest Increasing Path in a Matrix
#

# @lc code=start
from typing import List
from collections import namedtuple


class Node:
    def __init__(self, position, color='white', adjs=None, max_depth=0):
        self.position = position
        self.color = color
        if not adjs:
            adjs = []
        self.adjs = adjs
        self.max_depth = max_depth


Position = namedtuple('Position', 'i j')


class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        if not matrix:
            return 0
        nodes = {}
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                value = matrix[i][j]
                position = Position(i, j)
                adjs = []
                if i > 0 and matrix[i-1][j] > value:
                    adjs.append(Position(i-1, j))
                if i < len(matrix)-1 and matrix[i+1][j] > value:
                    adjs.append(Position(i+1, j))
                if j > 0 and matrix[i][j-1] > value:
                    adjs.append(Position(i, j-1))
                if j < len(matrix[i])-1 and matrix[i][j+1] > value:
                    adjs.append(Position(i, j+1))
                nodes[position] = Node(position, adjs=adjs)

        def dfs_visit(node):
            node.color = 'gray'
            for adj_position in node.adjs:
                adj = nodes[adj_position]
                if adj.color == 'white':
                    dfs_visit(adj)
                node.max_depth = max(adj.max_depth+1, node.max_depth)
            node.color = 'black'

        max_depth = 0
        for node in nodes.values():
            if node.color == 'white':
                dfs_visit(node)
                max_depth = max(max_depth, node.max_depth)
        return max_depth + 1


# @lc code=end

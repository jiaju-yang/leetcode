#
# @lc app=leetcode id=133 lang=python3
#
# [133] Clone Graph
#
from .graph_tools import *

# @lc code=start


class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return None
        cloned = {}

        def clone(node):
            if node.val in cloned:
                return cloned[node.val]
            copy = Node(node.val)
            cloned[copy.val] = copy
            for adj in node.neighbors:
                copy.neighbors.append(clone(adj))
            return copy
        return clone(node)

# @lc code=end


solve = Solution().cloneGraph


def test_default():
    assert is_graph_equal(solve(construct_graph_from_adj_list(
        [[2, 4], [1, 3], [2, 4], [1, 3]])), construct_graph_from_adj_list(
        [[2, 4], [1, 3], [2, 4], [1, 3]]))


def test_corners():
    assert is_graph_equal(solve(construct_graph_from_adj_list(
        [[]])), construct_graph_from_adj_list(
        [[]]))
    assert is_graph_equal(solve(construct_graph_from_adj_list(
        [])), construct_graph_from_adj_list(
        []))
    assert is_graph_equal(solve(construct_graph_from_adj_list(
        [[2], [1]])), construct_graph_from_adj_list(
        [[2], [1]]))

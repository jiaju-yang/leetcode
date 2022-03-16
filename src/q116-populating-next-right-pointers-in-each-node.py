#
# @lc app=leetcode id=116 lang=python3
#
# [116] Populating Next Right Pointers in Each Node
#
from .tree_tools import *
from typing import Optional


# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

# @lc code=start


class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        levels = []
        cur = root
        while cur:
            levels.append(cur)
            cur = cur.left
        self.dfs(root, levels, 0)
        return root

    def dfs(self, node, levels, cur_level):
        if not node:
            return
        if levels[cur_level] != node:
            levels[cur_level].next = node
            levels[cur_level] = node
        self.dfs(node.left, levels, cur_level+1)
        self.dfs(node.right, levels, cur_level+1)


# @lc code=end
solve = Solution().connect


def test_default():
    tree = solve(construct_tree([1, 2, 3, 4, 5, 6, 7]))
    assert tree.left.next is tree.right
    assert tree.left.left.next is tree.left.right
    assert tree.left.right.next is tree.right.left
    assert tree.right.left.next is tree.right.right
    assert tree.next is None
    assert tree.right.next is None
    assert tree.right.right.next is None


def test_corner_cases():
    tree = solve(construct_tree([1]))
    assert tree.next is None

    tree = solve(construct_tree([]))
    assert tree is None

#
# @lc app=leetcode id=226 lang=python3
#
# [226] Invert Binary Tree
#
from .tree_tools import *
from typing import Optional

# @lc code=start


class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        return self.dfs(root)

    def dfs(self, node):
        if not node:
            return
        node.left, node.right = self.dfs(node.right), self.dfs(node.left)
        return node


# @lc code=end
solve = Solution().invertTree


def test_default():
    assert solve(construct_tree([4, 2, 7, 1, 3, 6, 9])
                 ) == construct_tree([4, 7, 2, 9, 6, 3, 1])
    assert solve(construct_tree([2, 1, 3])) == construct_tree([2, 3, 1])


def test_corner_cases():
    assert solve(construct_tree([])) == construct_tree([])
    assert solve(construct_tree([1])) == construct_tree([1])
    assert not solve(construct_tree([1])) == construct_tree([2])

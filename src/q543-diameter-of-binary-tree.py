#
# @lc app=leetcode id=543 lang=python3
#
# [543] Diameter of Binary Tree
#
from typing import Optional
from .tree_tools import *

# @lc code=start


class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        diam, _ = self.max_diam_and_depth(root)
        return diam - 1

    def max_diam_and_depth(self, node):
        if not node:
            return 0, 0
        left_diam, left_depth = self.max_diam_and_depth(node.left)
        right_diam, right_depth = self.max_diam_and_depth(node.right)
        return max(left_diam, right_diam, left_depth + right_depth + 1), max(left_depth, right_depth) + 1


# @lc code=end
solve = Solution().diameterOfBinaryTree


def test_default():
    assert solve(construct_tree([1, 2, 3, 4, 5])) == 3
    assert solve(construct_tree([1, 2])) == 1


def test_corner_cases():
    assert solve(construct_tree([1])) == 0

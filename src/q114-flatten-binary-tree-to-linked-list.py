#
# @lc app=leetcode id=114 lang=python3
#
# [114] Flatten Binary Tree to Linked List
#
from typing import Optional
from .tree_tools import *

# @lc code=start


class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return
        left = root.left
        right = root.right
        root.left = None
        root.right = None
        if left:
            self.flatten(left)
            root.left = None
            root.right = left
        if right:
            self.flatten(right)
            right_most = self.find_the_right_most(root)
            right_most.right = right

    def find_the_right_most(self, node):
        if not node.right:
            return node
        return self.find_the_right_most(node.right)


# @lc code=end
solve = Solution().flatten


def test_default():
    tree = construct_tree([1, 2, 5, 3, 4, None, 6])
    solve(tree)
    assert (tree.val == 1 and tree.right.val == 2
            and tree.right.right.val == 3
            and tree.right.right.right.val == 4
            and tree.right.right.right.right.val == 5
            and tree.right.right.right.right.right.val == 6
            )


def test_corner_cases():
    tree = construct_tree([0])
    solve(tree)
    assert (tree.val == 0 and tree.right is None and tree.left is None)

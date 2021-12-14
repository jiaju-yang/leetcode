#
# @lc app=leetcode id=572 lang=python3
#
# [572] Subtree of Another Tree
#
from .tree_tools import *
from typing import Optional

# @lc code=start


class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot:
            return True
        if not root:
            return False
        if self.is_same(root, subRoot):
            return True
        if self.isSubtree(root.left, subRoot):
            return True
        if self.isSubtree(root.right, subRoot):
            return True
        return False

    def is_same(self, nodea, nodeb):
        if nodea and nodeb:
            return nodea.val == nodeb.val and self.is_same(nodea.left, nodeb.left) and self.is_same(nodea.right, nodeb.right)
        return nodea is nodeb


# @lc code=end
solve = Solution().isSubtree


def test_default():
    assert solve(construct_tree([3, 4, 5, 1, 2]), construct_tree([4, 1, 2]))
    assert not solve(construct_tree(
        [3, 4, 5, 1, 2, None, None, None, None, 0]), construct_tree([4, 1, 2]))


def test_corner_cases():
    assert solve(None, None)
    assert solve(construct_tree([1]), construct_tree([1]))
    assert solve(construct_tree([2, 1]), construct_tree([1]))
    assert not solve(construct_tree([1, 2]), construct_tree([1]))

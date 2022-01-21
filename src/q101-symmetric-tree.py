#
# @lc app=leetcode id=101 lang=python3
#
# [101] Symmetric Tree
#
from copyreg import constructor
from typing import Optional
from .tree_tools import *

# @lc code=start


class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        return self.is_equal(root.left, root.right)

    def is_equal(self, tree1, tree2):
        if tree1 and tree2:
            return tree1.val == tree2.val and self.is_equal(tree1.left, tree2.right) and self.is_equal(tree1.right, tree2.left)
        return tree1 is tree2


# @lc code=end
solve = Solution().isSymmetric


def test_default():
    assert solve(construct_tree([1, 2, 2, 3, 4, 4, 3]))
    assert not solve(construct_tree([1, 2, 2, None, 3, None, 3]))


def test_corner_cases():
    assert solve(construct_tree([1]))
    assert not solve(construct_tree([1, 2]))
    assert not solve(construct_tree([1, None, 2]))
    assert solve(construct_tree([1, 2, 2]))

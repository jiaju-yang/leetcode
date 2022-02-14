#
# @lc app=leetcode id=617 lang=python3
#
# [617] Merge Two Binary Trees
#
from typing import Optional
from .tree_tools import *

# @lc code=start


class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root1 and not root2:
            return None
        if root1 and root2:
            new_root = TreeNode(val=root1.val + root2.val)
            new_root.left = self.mergeTrees(root1.left, root2.left)
            new_root.right = self.mergeTrees(root1.right, root2.right)
            return new_root
        return root1 if root1 else root2


# @lc code=end
solve = Solution().mergeTrees


def test_default():
    assert solve(construct_tree([1, 3, 2, 5]), construct_tree(
        [2, 1, 3, None, 4, None, 7])) == construct_tree([3, 4, 5, 5, 4, None, 7])


def test_corner_cases():
    assert solve(construct_tree([1]), construct_tree(
        [2])) == construct_tree([3])
    assert solve(construct_tree([1]), construct_tree(
        [1, 2])) == construct_tree([2, 2])
    assert solve(None, construct_tree([1])) == construct_tree([1])
    assert solve(construct_tree([1]), None) == construct_tree([1])

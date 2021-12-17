#
# @lc app=leetcode id=235 lang=python3
#
# [235] Lowest Common Ancestor of a Binary Search Tree
#
from .tree_tools import *
# @lc code=start


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if p.val < root.val and q.val < root.val:
            return self.lowestCommonAncestor(root.left, p, q)
        if p.val > root.val and q.val > root.val:
            return self.lowestCommonAncestor(root.right, p, q)
        return TreeNode(root.val)


# @lc code=end
solve = Solution().lowestCommonAncestor


def test_default():
    assert solve(construct_tree([6, 2, 8, 0, 4, 7, 9, None, None, 3, 5]), TreeNode(
        2), TreeNode(8)) == TreeNode(6)
    assert solve(construct_tree([6, 2, 8, 0, 4, 7, 9, None, None, 3, 5]), TreeNode(
        2), TreeNode(4)) == TreeNode(2)


def test_corner_cases():
    assert solve(construct_tree(
        [2, 1]), TreeNode(2), TreeNode(1)) == TreeNode(2)

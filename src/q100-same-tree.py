#
# @lc app=leetcode id=100 lang=python3
#
# [100] Same Tree
#
from .tree_tools import *
from typing import Optional

# @lc code=start


class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        return self.dfs(p, q)

    def dfs(self, nodea, nodeb):
        if nodea is None and nodeb is None:
            return True
        if nodea is not None and nodeb is not None:
            if nodea.val != nodeb.val:
                return False
            return self.dfs(nodea.left, nodeb.left) and self.dfs(nodea.right, nodeb.right)
        return False
# @lc code=end


solve = Solution().isSameTree


def test_default():
    assert solve(construct_tree([1, 2, 3]), construct_tree([1, 2, 3]))
    assert not solve(construct_tree([1, 2]), construct_tree([1, None, 2]))
    assert not solve(construct_tree([1, 2, 1]), construct_tree([1, 1, 2]))


def test_corner_cases():
    assert solve(construct_tree([1]), construct_tree([1]))
    assert not solve(construct_tree([1]), construct_tree([2]))
    assert solve(construct_tree([]), construct_tree([]))

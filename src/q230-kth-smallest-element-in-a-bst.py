#
# @lc app=leetcode id=230 lang=python3
#
# [230] Kth Smallest Element in a BST
#
from .tree_tools import *
from typing import Optional

# @lc code=start


class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        l = []
        self.dfs(root, l)
        return l[k-1]

    def dfs(self, node, q):
        if not node:
            return
        self.dfs(node.left, q)
        q.append(node.val)
        self.dfs(node.right, q)
# @lc code=end


solve = Solution().kthSmallest


def test_default():
    assert solve(construct_tree([3, 1, 4, None, 2]), 1) == 1
    assert solve(construct_tree([5, 3, 6, 2, 4, None, None, 1]), 3) == 3


def test_corner_cases():
    assert solve(construct_tree([1]), 1) == 1
    assert solve(construct_tree([1, None, 2]), 2) == 2

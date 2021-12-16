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
        return self.dfs(root, [], k)

    def dfs(self, node, q, k):
        if not node:
            return
        count = self.dfs(node.left, q, k)
        if count is not None:
            return count
        q.append(node.val)
        if len(q) == k:
            return node.val
        count = self.dfs(node.right, q, k)
        if count is not None:
            return count

# @lc code=end


solve = Solution().kthSmallest


def test_default():
    assert solve(construct_tree([3, 1, 4, None, 2]), 1) == 1
    assert solve(construct_tree([5, 3, 6, 2, 4, None, None, 1]), 3) == 3


def test_corner_cases():
    assert solve(construct_tree([1]), 1) == 1
    assert solve(construct_tree([1, None, 2]), 2) == 2

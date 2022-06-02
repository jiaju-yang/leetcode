#
# @lc app=leetcode id=230 lang=python3
#
# [230] Kth Smallest Element in a BST
#
from .tree_tools import *
from typing import Optional


class RecursviveSolution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        remain = k

        def dfs(node):
            if not node:
                return
            result = dfs(node.left)
            if result is not None:
                return result
            nonlocal remain
            remain -= 1
            if remain == 0:
                return node.val
            result = dfs(node.right)
            if result is not None:
                return result

        return dfs(root)

# @lc code=start


class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stack = []
        cur = root
        while cur or stack:
            while cur:
                stack.append(cur)
                cur = cur.left
            k -= 1
            cur = stack.pop()
            if k == 0:
                return cur.val
            cur = cur.right


# @lc code=end


solve = Solution().kthSmallest


def test_default():
    assert solve(construct_tree([3, 1, 4, None, 2]), 1) == 1
    assert solve(construct_tree([5, 3, 6, 2, 4, None, None, 1]), 3) == 3


def test_corner_cases():
    assert solve(construct_tree([1]), 1) == 1
    assert solve(construct_tree([1, None, 2]), 2) == 2

#
# @lc app=leetcode id=114 lang=python3
#
# [114] Flatten Binary Tree to Linked List
#
from typing import Optional
from .tree_tools import *


class DFSSolution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return
        return self.dfs(root)[0]

    def dfs(self, node):
        left, right = node.left, node.right
        tail = node
        if left:
            left_head, tail = self.dfs(left)
            node.left = None
            node.right = left_head
        if right:
            right_head, new_tail = self.dfs(right)
            tail.right = right_head
            tail = new_tail
        return node, tail

# @lc code=start


class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        if not root:
            return
        stack = [root]
        while stack:
            node = stack.pop()
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
            node.left = None
            node.right = stack[-1] if stack else None


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

    tree = None
    solve(tree)
    assert tree is None

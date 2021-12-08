#
# @lc app=leetcode id=104 lang=python3
#
# [104] Maximum Depth of Binary Tree
#
from typing import Optional
from collections import deque
from .tree_tools import *


class BFSSolution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        return self.bfs(root)

    def bfs(self, root):
        level = 1
        q = deque([(root, level)])
        while q:
            node, level = q.pop()
            if node.left:
                q.appendleft((node.left, level + 1))
            if node.right:
                q.appendleft((node.right, level + 1))
        return level

# @lc code=start


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        return self.dfs(root)

    def dfs(self, node):
        if not node:
            return 0
        return max(self.dfs(node.left), self.dfs(node.right)) + 1


# @lc code=end
solve = Solution().maxDepth


def test_default():
    assert solve(construct_tree([3, 9, 20, None, None, 15, 7])) == 3
    assert solve(construct_tree([1, None, 2])) == 2


def test_corner_cases():
    assert solve(None) == 0
    assert solve(construct_tree([0])) == 1

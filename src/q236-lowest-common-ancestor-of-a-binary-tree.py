#
# @lc app=leetcode id=236 lang=python3
#
# [236] Lowest Common Ancestor of a Binary Tree
#
from .tree_tools import *

# @lc code=start


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        p_path, q_path = [], []
        self.dfs(root, p, p_path)
        self.dfs(root, q, q_path)
        lowest = None
        for p_node, q_node in zip(p_path, q_path):
            if p_node is q_node:
                lowest = p_node
            else:
                break
        return lowest

    def dfs(self, root, target, path):
        if not root:
            return False
        path.append(root)
        if root is target:
            return True
        if self.dfs(root.left, target, path):
            return True
        if self.dfs(root.right, target, path):
            return True
        path.pop()
        return False
# @lc code=end

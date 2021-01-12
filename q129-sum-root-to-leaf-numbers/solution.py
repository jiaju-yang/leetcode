#
# @lc app=leetcode id=129 lang=python3
#
# [129] Sum Root to Leaf Numbers
#

# @lc code=start
from collections import deque
# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class DFSSolution:
    def sumNumbers(self, root: TreeNode) -> int:
        def dfs_visit(node, path):
            if not node:
                return
            curr_path = path + [str(node.val)]
            if not node.left and not node.right:
                num = int(''.join(curr_path))
                nonlocal result
                result += num
                return
            dfs_visit(node.left, curr_path)
            dfs_visit(node.right, curr_path)
        result = 0
        dfs_visit(root, [])
        return result


class BFSSolution:
    def sumNumbers(self, root: TreeNode) -> int:
        if not root:
            return 0
        q = deque([(root, [])])
        result = 0
        while q:
            node, path = q.pop()
            curr_path = path + [str(node.val)]
            if not node.left and not node.right:
                num = int(''.join(curr_path))
                result += num
            if node.left:
                q.appendleft((node.left, curr_path))
            if node.right:
                q.appendleft((node.right, curr_path))
        return result


Solution = BFSSolution
# @lc code=end

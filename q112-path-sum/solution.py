#
# @lc app=leetcode id=112 lang=python3
#
# [112] Path Sum
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
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        def dfs_visit(node, remain):
            if not node:
                return False
            curr_remain = remain - node.val
            if not curr_remain and not node.left and not node.right:
                return True
            return dfs_visit(node.left, curr_remain) or dfs_visit(node.right, curr_remain)
        return dfs_visit(root, sum)


class BFSSolution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if not root:
            return False
        q = deque([(root, sum)])
        while q:
            node, remain = q.pop()
            if not node.left and not node.right and node.val == remain:
                return True
            if node.left:
                q.appendleft((node.left, remain-node.val))
            if node.right:
                q.appendleft((node.right, remain-node.val))
        return False


Solution = BFSSolution
# @lc code=end

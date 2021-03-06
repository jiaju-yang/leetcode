#
# @lc app=leetcode id=102 lang=python3
#
# [102] Binary Tree Level Order Traversal
#

# @lc code=start
# Definition for a binary tree node.
from typing import List
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class BFSSolution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        result = []
        if not root:
            return result
        q = deque([root])
        while q:
            vals = []
            for _ in range(len(q)):
                node = q.popleft()
                vals.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            result.append(vals)
        return result


class DFSSolution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        result = []

        def driver(node, i):
            if not node:
                return
            try:
                result[i].append(node.val)
            except:
                result.append([node.val])
            driver(node.left, i+1)
            driver(node.right, i+1)
        driver(root, 0)
        return result


Solution = DFSSolution
# @lc code=end

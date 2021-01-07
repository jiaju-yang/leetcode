#
# @lc app=leetcode id=637 lang=python3
#
# [637] Average of Levels in Binary Tree
#

# @lc code=start
from typing import List
from collections import deque
# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class BFSSolution:
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        result = []
        if not root:
            return result
        q = deque([root])
        while q:
            count = len(q)
            level_sum = 0
            for _ in range(count):
                node = q.popleft()
                level_sum += node.val
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            result.append(level_sum/count)
        return result


class DFSSolution:
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        def dfs_visit(node, level):
            if not node:
                return
            try:
                result[level].append(node.val)
            except IndexError:
                result.append([node.val])
            dfs_visit(node.left, level+1)
            dfs_visit(node.right, level+1)
        result = []
        dfs_visit(root, 0)
        return [sum(level)/len(level) for level in result]


Solution = DFSSolution
# @lc code=end

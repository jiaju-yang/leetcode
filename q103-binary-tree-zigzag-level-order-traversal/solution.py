#
# @lc app=leetcode id=103 lang=python3
#
# [103] Binary Tree Zigzag Level Order Traversal
#
# @lc code=start
# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class BFSSolution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        result = []
        if not root:
            return result
        current_level = [root]
        left_to_right = True
        while current_level:
            if left_to_right:
                result.append([node.val for node in current_level])
            else:
                result.append([node.val for node in reversed(current_level)])
            pairs = ((node.left, node.right)
                     for node in current_level)
            current_level = [i for pair in pairs
                             for i in pair if i]
            left_to_right = not left_to_right
        return result


class DFSSolution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        result = []

        def driver(node, i):
            if not node:
                return
            try:
                result[i].insert(0 if i % 2 == 1 else len(result[i]), node.val)
            except:
                result.append([node.val])
            driver(node.left, i + 1)
            driver(node.right, i + 1)
        driver(root, 0)
        return result


Solution = BFSSolution
# @lc code=end

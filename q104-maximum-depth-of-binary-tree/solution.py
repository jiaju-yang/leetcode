#
# @lc app=leetcode id=104 lang=python3
#
# [104] Maximum Depth of Binary Tree
#
# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class BFSSolution:
    def maxDepth(self, root: TreeNode) -> int:
        depth = 0
        if not root:
            return depth
        current_level = [root]
        while current_level:
            if current_level:
                depth += 1
            pairs = ((node.left, node.right) for node in current_level)
            current_level = [child for pair in pairs
                             for child in pair if child]
        return depth


class DFSSolution:
    def maxDepth(self, root: TreeNode) -> int:
        depth = 0

        def driver(node, i):
            if not node:
                return
            nonlocal depth
            depth = max(depth, i)
            driver(node.left, i + 1)
            driver(node.right, i + 1)
        driver(root, 1)
        return depth


class AnotherDFSSolution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))


Solution = AnotherDFSSolution
# @lc code=end

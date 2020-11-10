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


Solution = BFSSolution
# @lc code=end

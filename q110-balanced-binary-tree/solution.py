#
# @lc app=leetcode id=110 lang=python3
#
# [110] Balanced Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class DFSSolution:
    def isBalanced(self, root: TreeNode) -> bool:
        def dfs_visit(node):
            if not node:
                return True, 0
            left_balanced, left_height = dfs_visit(node.left)
            right_balanced, right_height = dfs_visit(node.right)
            balanced = False
            if left_balanced and right_balanced and abs(left_height-right_height) <= 1:
                balanced = True
            return balanced, max(left_height, right_height) + 1
        return dfs_visit(root)[0]


class AnotherDFSSolution:
    def isBalanced(self, root: TreeNode) -> bool:
        def dfs_visit(node):
            if not node:
                return 0
            left_height = dfs_visit(node.left)
            if left_height < 0:
                return -1
            right_height = dfs_visit(node.right)
            if right_height < 0:
                return -1
            if abs(left_height - right_height) > 1:
                return -1
            return max(left_height, right_height) + 1
        return False if dfs_visit(root) < 0 else True


Solution = AnotherDFSSolution
# @lc code=end

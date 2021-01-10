#
# @lc app=leetcode id=113 lang=python3
#
# [113] Path Sum II
#

# @lc code=start
from typing import List
# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        def dfs_visit(node, remain, path):
            if not node:
                return
            curr_remain = remain - node.val
            curr_path = path[:] + [node.val]
            if not node.left and not node.right and curr_remain == 0:
                result.append(curr_path)
                return
            dfs_visit(node.left, curr_remain, curr_path)
            dfs_visit(node.right, curr_remain, curr_path)
        result = []
        dfs_visit(root, sum, [])
        return result

# @lc code=end

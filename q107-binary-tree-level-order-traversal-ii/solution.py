#
# @lc app=leetcode id=107 lang=python3
#
# [107] Binary Tree Level Order Traversal II
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


class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        root.level = 0
        q = deque([root])
        result = []
        while q:
            cur = q.pop()
            if cur.left:
                cur.left.level = cur.level+1
                q.appendleft(cur.left)
            if cur.right:
                cur.right.level = cur.level+1
                q.appendleft(cur.right)
            try:
                result[cur.level].append(cur.val)
            except IndexError:
                result.append([cur.val])
        return result[::-1]
# @lc code=end

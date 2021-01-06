#
# @lc app=leetcode id=111 lang=python3
#
# [111] Minimum Depth of Binary Tree
#

# @lc code=start
from collections import deque
# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def minDepth(self, root: TreeNode) -> int:
        min_depth = 0
        if not root:
            return min_depth
        q = deque([root])
        while q:
            min_depth += 1
            for _ in range(len(q)):
                node = q.popleft()
                if not node.left and not node.right:
                    return min_depth
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)


# @lc code=end

#
# @lc app=leetcode id=105 lang=python3
#
# [105] Construct Binary Tree from Preorder and Inorder Traversal
#
from typing import List, Optional
from .tree_tools import *

# @lc code=start


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder:
            return None
        node = TreeNode(preorder[0])
        length = inorder.index(preorder[0])
        node.left = self.buildTree(preorder[1:1+length], inorder[:length])
        node.right = self.buildTree(preorder[1+length:], inorder[length+1:])
        return node


# @lc code=end
solve = Solution().buildTree


def test_default():
    solve([3, 9, 20, 15, 7], [9, 3, 15, 20, 7]) == construct_tree(
        [3, 9, 20, None, None, 15, 7])


def test_corner_cases():
    solve([-1], [-1]) == TreeNode(-1)
    solve([], []) == None
    solve([1, 2], [2, 1]) == construct_tree([1, 2])

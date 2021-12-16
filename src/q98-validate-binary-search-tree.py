#
# @lc app=leetcode id=98 lang=python3
#
# [98] Validate Binary Search Tree
#
from .tree_tools import *
from typing import Optional

# @lc code=start


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.dfs(root, float('-inf'), float('inf'))

    def dfs(self, node, minimum, maximum):
        if not node:
            return True
        if node.val >= maximum or node.val <= minimum:
            return False
        return self.dfs(node.left, minimum, node.val) and self.dfs(node.right, node.val, maximum)


# @lc code=end
solve = Solution().isValidBST


def test_default():
    assert solve(construct_tree([2, 1, 3]))
    assert not solve(construct_tree([5, 1, 4, None, None, 3, 6]))


def test_corner_cases():
    assert solve(construct_tree([1]))
    assert not solve(construct_tree([1, 2]))
    assert solve(construct_tree([1, None, 2]))
    assert not solve(construct_tree([2, 2, 2]))

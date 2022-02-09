#
# @lc app=leetcode id=337 lang=python3
#
# [337] House Robber III
#
from typing import Optional
from .tree_tools import *

# @lc code=start


class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        return max(self.max_include_and_exclude(root))

    def max_include_and_exclude(self, node):
        if not node:
            return 0, 0
        left_include, left_exclude = self.max_include_and_exclude(node.left)
        right_include, right_exclude = self.max_include_and_exclude(node.right)
        return left_exclude + right_exclude + node.val, max(left_include, left_exclude) + max(right_include, right_exclude)


# @lc code=end
solve = Solution().rob


def test_default():
    assert solve(construct_tree([3, 2, 3, None, 3, None, 1])) == 7
    assert solve(construct_tree([3, 4, 5, 1, 3, None, 1])) == 9


def test_corner_cases():
    assert solve(construct_tree([1])) == 1
    assert solve(construct_tree([1, 2])) == 2
    assert solve(construct_tree([1, 2, 3])) == 5

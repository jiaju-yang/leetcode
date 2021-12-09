#
# @lc app=leetcode id=124 lang=python3
#
# [124] Binary Tree Maximum Path Sum
#
from .tree_tools import *
from typing import Optional

# @lc code=start


class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        max_sum = root.val

        def max_path(node):
            if not node:
                return 0
            left_max = max_path(node.left)
            right_max = max_path(node.right)
            nonlocal max_sum
            max_sum = max(max_sum, left_max + node.val + right_max)
            return max(0, left_max + node.val, right_max + node.val)
        max_path(root)
        return max_sum


# @lc code=end
solve = Solution().maxPathSum


def test_default():
    assert solve(construct_tree([1, 2, 3])) == 6
    assert solve(construct_tree([-10, 9, 20, None, None, 15, 7])) == 42


def test_corner_cases():
    assert solve(construct_tree([1])) == 1
    assert solve(construct_tree([-1])) == -1
    assert solve(construct_tree([-1, 2])) == 2

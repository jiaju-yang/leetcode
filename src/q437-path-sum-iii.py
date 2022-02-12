#
# @lc app=leetcode id=437 lang=python3
#
# [437] Path Sum III
#
from typing import Optional
from .tree_tools import *


# @lc code=start

class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        return self.paths(root, targetSum)[0]

    def paths(self, node, target):
        new_paths = []
        new_count = 0
        if not node:
            return new_count, new_paths
        new_paths.append(node.val)
        if node.val == target:
            new_count += 1
        if node.left:
            count, paths = self.paths(node.left, target)
            new_count += count
            for path in paths:
                new_sum = path + node.val
                if new_sum == target:
                    new_count += 1
                new_paths.append(new_sum)
        if node.right:
            count, paths = self.paths(node.right, target)
            new_count += count
            for path in paths:
                new_sum = path + node.val
                if new_sum == target:
                    new_count += 1
                new_paths.append(new_sum)
        return new_count, new_paths


# @lc code=end
solve = Solution().pathSum


def test_default():
    assert solve(construct_tree(
        [10, 5, -3, 3, 2, None, 11, 3, -2, None, 1]), 8) == 3
    assert solve(construct_tree(
        [5, 4, 8, 11, None, 13, 4, 7, 2, None, None, 5, 1]), 22) == 3


def test_corner_cases():
    assert solve(construct_tree([1]), 1) == 1
    assert solve(construct_tree([]), 1) == 0
    assert solve(construct_tree([2]), 1) == 0
    assert solve(construct_tree([1, 2]), 3) == 1
    assert solve(construct_tree([0, 0]), 0) == 3

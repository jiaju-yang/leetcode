#
# @lc app=leetcode id=102 lang=python3
#
# [102] Binary Tree Level Order Traversal
#
from .tree_tools import *
from typing import Optional, List

# @lc code=start


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        result = []
        self.dfs(root, 0, result)
        return result

    def dfs(self, node, level, result):
        if not node:
            return
        if level == len(result):
            result.append([])
        result[level].append(node.val)
        self.dfs(node.left, level+1, result)
        self.dfs(node.right, level+1, result)

# @lc code=end


solve = Solution().levelOrder


def test_default():
    assert solve(construct_tree([3, 9, 20, None, None, 15, 7])) == [
        [3], [9, 20], [15, 7]]


def test_corner_cases():
    assert solve(construct_tree([1])) == [[1]]
    assert solve(construct_tree([1, 2])) == [[1], [2]]
    assert solve(None) == []

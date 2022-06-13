#
# @lc app=leetcode id=94 lang=python3
#
# [94] Binary Tree Inorder Traversal
#
from .tree_tools import *
from typing import Optional, List

# @lc code=start


class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        stack = []
        ret = []
        cur = root
        while cur or stack:
            while cur:
                stack.append(cur)
                cur = cur.left
            cur = stack.pop()
            ret.append(cur.val)
            cur = cur.right
        return ret


# @lc code=end
solve = Solution().inorderTraversal


def test_default():
    assert solve(construct_tree([1, 2, None, 3, 4])) == [3, 2, 4, 1]


def test_corner_cases():
    assert solve(construct_tree([1])) == [1]
    assert solve(None) == []

#
# @lc app=leetcode id=297 lang=python3
#
# [297] Serialize and Deserialize Binary Tree
#
from .tree_tools import *
from collections import deque

# @lc code=start


class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        return f'{root.val},{self.serialize(root.left)},{self.serialize(root.right)}' if root else ''

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        return self.preorder(deque(data.split(',')))

    def preorder(self, q):
        val = q.popleft()
        if val == '':
            return None
        node = TreeNode(int(val))
        node.left = self.preorder(q)
        node.right = self.preorder(q)
        return node


# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
# @lc code=end
solution = Codec()


def test_default():
    assert solution.deserialize(solution.serialize(construct_tree(
        [1, 2, 3, None, None, 4, 5]))) == construct_tree([1, 2, 3, None, None, 4, 5])


def test_corner_cases():
    assert solution.deserialize(solution.serialize(None)) == None
    assert solution.deserialize(solution.serialize(construct_tree(
        [1]))) == construct_tree([1])
    assert solution.deserialize(solution.serialize(construct_tree(
        [1, 2]))) == construct_tree([1, 2])

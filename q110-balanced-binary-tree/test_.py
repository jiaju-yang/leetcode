from collections import deque
from solution import Solution, TreeNode

solve = Solution().isBalanced


def construct_tree(values):
    if not values:
        return None
    root = TreeNode(values[0])
    nodes = deque([root])
    for i in range(1, len(values), 2):
        current = nodes.pop()
        if values[i] is not None:
            current.left = TreeNode(values[i])
            nodes.appendleft(current.left)
        if values[i+1] is not None:
            current.right = TreeNode(values[i+1])
            nodes.appendleft(current.right)
    return root


def test_default():
    assert solve(construct_tree([3, 9, 20, None, None, 15, 7])) is True


def test_corner_cases():
    assert solve(construct_tree([])) is True
    assert solve(construct_tree([1])) is True
    assert solve(construct_tree([1, 2, None])) is True


def test_non_balanced_cases():
    assert solve(construct_tree([1, 2, 2, 3, 3, None, None, 4, 4])) is False

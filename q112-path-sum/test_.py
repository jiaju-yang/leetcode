from collections import deque
from solution import Solution, TreeNode

solve = Solution().hasPathSum


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
    assert solve(construct_tree(
        [5, 4, 8, 11, None, 13, 4, 7, 2, None, 1]), 22) is True


def test_corner_cases():
    assert solve(construct_tree([]), 0) is False
    assert solve(construct_tree([1]), 1) is True
    assert solve(construct_tree([1, 2, None]), 3) is True


def test_failures():
    assert solve(construct_tree([]), 1) is False
    assert solve(construct_tree([1]), 2) is False
    assert solve(construct_tree([1, 2, None]), 1) is False

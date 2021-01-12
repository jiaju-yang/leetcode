from collections import deque
from solution import Solution, TreeNode

solve = Solution().sumNumbers


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
    assert solve(construct_tree([1, 2, 3])) == 25
    assert solve(construct_tree([4, 9, 0, 5, 1])) == 1026


def test_corner_cases():
    assert solve(construct_tree([])) == 0
    assert solve(construct_tree([1])) == 1
    assert solve(construct_tree([1, 2, None])) == 12

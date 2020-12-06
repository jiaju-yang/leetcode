from solution import Solution

solve = Solution().canFinish


def test_default():
    assert solve(2, [[1, 0]]) is True
    assert solve(3, [[1, 0], [2, 0]]) is True
    assert solve(8, [[1, 0], [2, 6], [1, 7], [6, 4], [7, 0], [0, 5]]) is True


def test_corner_cases():
    assert solve(0, []) is True
    assert solve(1, []) is True


def test_failure_cases():
    assert solve(2, [[1, 0], [0, 1]]) is False
    assert solve(3, [[1, 0], [1, 2], [0, 1]]) is False
    assert solve(3, [[0, 2], [1, 2], [2, 0]]) is False

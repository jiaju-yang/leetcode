from solution import Solution

solve = Solution().canFinish


def test_default():
    assert solve(2, [[1, 0]]) is True


def test_corner_cases():
    assert solve(0, []) is True


def test_failure_cases():
    assert solve(2, [[1, 0], [0, 1]]) is False

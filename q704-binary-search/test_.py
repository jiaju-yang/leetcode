from solution import Solution

solve = Solution().search


def test_default():
    assert solve([-1, 0, 3, 5, 9, 12], 9) == 4


def test_corner_cases():
    assert solve([1], 1) == 0
    assert solve([], 0) == -1
    assert solve([1], 0) == -1


def test_failure_cases():
    assert solve([-1, 0, 3, 5, 9, 12], 2) == -1

from solution import Solution

solve = Solution().threeSum


def test_default():
    assert solve([-1, 0, 1, 2, -1, -4]) == [[-1, -1, 2], [-1, 0, 1]]
    assert solve([-2, 0, 0, 2, 2]) == [[-2, 0, 2]]


def test_corner_cases():
    assert solve([]) == []
    assert solve([-2, 1, 1]) == [[-2, 1, 1]]


def test_failure_cases():
    assert solve([0]) == []
    assert solve([-1, 2]) == []

from solution import Solution

solve = Solution().threeSumClosest


def test_default():
    assert solve([-1, 2, 1, -4], 1) == 2


def test_corner_cases():
    assert solve([-1, 0, 1], 1) == 0
    assert solve([0, 1, 2], 3) == 3

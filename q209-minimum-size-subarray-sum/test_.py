from solution import Solution

solve = Solution().minSubArrayLen


def test_default():
    assert solve(7, [2, 3, 1, 2, 4, 3]) == 2
    assert solve(11, [1, 2, 3, 4, 5]) == 3


def test_corner_cases():
    assert solve(1, [1]) == 1


def test_failure_cases():
    assert solve(5, [2, 1]) == 0
    assert solve(3, [1]) == 0

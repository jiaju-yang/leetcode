from solution import Solution

solve = Solution().findKthLargest


def test_default():
    assert solve([3, 2, 1, 5, 6, 4], 2) == 5
    assert solve([3, 2, 3, 1, 2, 4, 5, 5, 6], 4) == 4


def test_corner_cases():
    assert solve([1], 1) == 1
    assert solve([-1, -1], 2) == -1

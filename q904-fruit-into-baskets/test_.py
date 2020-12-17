from solution import Solution

solve = Solution().totalFruit


def test_default():
    assert solve([1, 2, 1]) == 3
    assert solve([0, 1, 2, 2]) == 3
    assert solve([3, 3, 3, 1, 2, 1, 1, 2, 3, 3, 4]) == 5
    assert solve([1, 2, 3, 2, 2]) == 4


def test_corner_cases():
    assert solve([0]) == 1
    assert solve([]) == 0

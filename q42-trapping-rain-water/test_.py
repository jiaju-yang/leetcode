from solution import Solution

solve = Solution().trap


def test_default():
    assert solve([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]) == 6
    assert solve([4, 2, 0, 3, 2, 5]) == 9


def test_corner_cases():
    assert solve([0, 0]) == 0
    assert solve([1, 1]) == 0
    assert solve([0, 1]) == 0
    assert solve([1]) == 0
    assert solve([0]) == 0
    assert solve([1, 0, 1]) == 1

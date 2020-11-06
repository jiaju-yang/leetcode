from solution import Solution

solve = Solution().missingNumber


def test_default():
    assert solve([3, 0, 1]) == 2
    assert solve([0, 1]) == 2
    assert solve([9, 6, 4, 2, 3, 5, 7, 0, 1]) == 8


def test_corner_cases():
    assert solve([0]) == 1
    assert solve([1]) == 0
    assert solve([]) == 0

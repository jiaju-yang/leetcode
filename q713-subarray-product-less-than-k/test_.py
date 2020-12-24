from solution import Solution

solve = Solution().numSubarrayProductLessThanK


def test_default():
    assert solve([10, 5, 2, 6], 100) == 8
    assert solve([10, 9, 10, 4, 3, 8, 3, 3, 6, 2, 10, 10, 9, 3], 19) == 18


def test_corner_cases():
    assert solve([2], 1) == 0
    assert solve([1], 1) == 0
    assert solve([1], 2) == 1
    assert solve([1, 2], 2) == 1
    assert solve([1, 2], 3) == 3

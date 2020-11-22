from solution import Solution

solve = Solution().singleNumber


def test_default():
    assert solve([2, 2, 1]) == 1
    assert solve([4, 1, 2, 1, 2]) == 4


def test_corner_cases():
    assert solve([1]) == 1
    assert solve([0]) == 0

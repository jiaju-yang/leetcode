from solution import Solution

solve = Solution().singleNumber


def test_default():
    assert solve([2, 2, 3, 2]) == 3
    assert solve([0, 1, 0, 1, 0, 1, 99]) == 99


def test_corner_cases():
    assert solve([1]) == 1
    assert solve([0]) == 0

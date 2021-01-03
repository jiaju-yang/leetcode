from solution import Solution

solve = Solution().findErrorNums


def test_default():
    assert solve([1, 2, 2, 4]) == [2, 3]


def test_corner_cases():
    assert solve([1, 1]) == [1, 2]
    assert solve([2, 2]) == [2, 1]

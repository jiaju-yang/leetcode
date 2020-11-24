from solution import Solution

solve = Solution().singleNumber


def test_default():
    assert solve([1, 2, 1, 3, 2, 5]) == [3, 5]


def test_corner_cases():
    assert solve([-1, 0]) == [-1, 0]
    assert solve([0, 1]) == [1, 0]

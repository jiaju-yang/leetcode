from solution import Solution

solve = Solution().subsets


def test_default():
    assert solve([1, 2, 3]) == [
        [], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]]


def test_corner_cases():
    assert solve([1]) == [[], [1]]

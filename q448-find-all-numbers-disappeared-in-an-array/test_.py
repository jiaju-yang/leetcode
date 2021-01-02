from solution import Solution

solve = Solution().findDisappearedNumbers


def test_default():
    assert solve([4, 3, 2, 7, 8, 2, 3, 1]) == [5, 6]


def test_corner_cases():
    assert solve([1]) == []
    assert solve([2, 2]) == [1]
    assert solve([]) == []

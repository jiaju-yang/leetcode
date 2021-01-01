from solution import Solution

solve = Solution().findDuplicates


def test_default():
    assert sorted(solve([4, 3, 2, 7, 8, 2, 3, 1])) == [2, 3]


def test_corner_cases():
    assert solve([0]) == []
    assert solve([]) == []
    assert solve([1, 1]) == [1]

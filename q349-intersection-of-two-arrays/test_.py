from solution import Solution

solve = Solution().intersection


def test_default():
    assert solve([1, 2, 2, 1], [2, 2]) == [2]
    assert set(solve([4, 9, 5], [9, 4, 9, 8, 4])) == set([9, 4])


def test_corner_cases():
    assert solve([1], []) == []
    assert solve([], []) == []
    assert solve([0], [0]) == [0]
    assert solve([0], [1]) == []

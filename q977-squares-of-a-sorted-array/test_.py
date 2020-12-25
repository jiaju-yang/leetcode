from solution import Solution

solve = Solution().sortedSquares


def test_default():
    assert solve([-4, -1, 0, 3, 10]) == [0, 1, 9, 16, 100]
    assert solve([-7, -3, 2, 3, 11]) == [4, 9, 9, 49, 121]


def test_corner_cases():
    assert solve([-1]) == [1]
    assert solve([0, 0]) == [0, 0]
    assert solve([]) == []

from solution import Solution

solve = Solution().findOrder


def test_default():
    assert solve(2, [[1, 0]]) == [0, 1]
    result = solve(4, [[1, 0], [2, 0], [3, 1], [3, 2]])
    assert result == [0, 1, 2, 3] or result == [0, 2, 1, 3]


def test_corner_cases():
    assert solve(1, []) == [0]


def test_failure_cases():
    assert solve(2, [[0, 1], [1, 0]]) == []

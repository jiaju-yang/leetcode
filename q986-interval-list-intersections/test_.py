from solution import Solution

solve = Solution().intervalIntersection


def test_default():
    assert solve([[0, 2], [5, 10], [13, 23], [24, 25]], [[1, 5], [8, 12], [15, 24], [
                 25, 26]]) == [[1, 2], [5, 5], [8, 10], [15, 23], [24, 24], [25, 25]]


def test_corner_cases():
    assert solve([], []) == []
    assert solve([[1, 2]], []) == []
    assert solve([], [[1, 2]]) == []
    assert solve([[1, 2]], [[2, 3]]) == [[2, 2]]

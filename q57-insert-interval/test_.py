from solution import Solution

solve = Solution().insert


def test_default():
    assert solve([[1, 3], [6, 9]], [2, 5]) == [[1, 5], [6, 9]]
    assert solve([[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]],
                 [4, 8]) == [[1, 2], [3, 10], [12, 16]]


def test_corner_cases():
    assert solve([], [5, 7]) == [[5, 7]]
    assert solve([[1, 5]], [2, 3]) == [[1, 5]]
    assert solve([[1, 5]], [2, 7]) == [[1, 7]]
    assert solve([[1, 5]], [6, 8]) == [[1, 5], [6, 8]]

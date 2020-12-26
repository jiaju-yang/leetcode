from solution import Solution

solve = Solution().longestIncreasingPath


def test_default():
    assert solve([
        [9, 9, 4],
        [6, 6, 8],
        [2, 1, 1]
    ]) == 4
    assert solve([
        [3, 4, 5],
        [3, 2, 6],
        [2, 2, 1]
    ]) == 4


def test_corner_cases():
    assert solve([]) == 0
    assert solve([[1]]) == 1

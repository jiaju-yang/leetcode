from solution import Solution

solve = Solution().orangesRotting


def test_default():
    assert solve([[2, 1, 1], [1, 1, 0], [0, 1, 1]]) == 4


def test_corner_cases():
    assert solve([[0, 2]]) == 0


def test_failure_cases():
    assert solve([[2, 1, 1], [0, 1, 1], [1, 0, 1]]) == -1

from solution import Solution

solve = Solution().longestOnes


def test_default():
    assert solve([1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0], 2) == 6
    assert solve([0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1,
                  1, 0, 0, 0, 1, 1, 1, 1], 3) == 10


def test_corner_cases():
    assert solve([1], 0) == 1
    assert solve([0], 1) == 1
    assert solve([0], 0) == 0

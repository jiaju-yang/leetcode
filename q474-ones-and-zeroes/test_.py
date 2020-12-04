from solution import Solution

solve = Solution().findMaxForm


def test_default():
    assert solve(['10', '0001', '111001', '1', '0'], 5, 3) == 4
    assert solve(['10', '0', '1'], 1, 1) == 2
    assert solve(['10', '0001', '111001', '1', '0'], 3, 4) == 3


def test_corner_cases():
    assert solve(['10'], 1, 1) == 1
    assert solve(['10'], 2, 1) == 1


def test_failure_cases():
    assert solve([], 1, 0) == 0

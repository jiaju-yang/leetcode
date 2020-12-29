from solution import Solution

solve = Solution().isHappy


def test_default():
    assert solve(19) is True
    assert solve(2) is False


def test_cornor_cases():
    assert solve(1) is True
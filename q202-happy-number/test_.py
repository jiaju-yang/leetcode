from solution import Solution

solve = Solution().isHappy


def test_default():
    assert solve(19) is True
    assert solve(2) is False

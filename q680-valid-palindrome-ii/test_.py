from solution import Solution

solve = Solution().validPalindrome


def test_default():
    assert solve('aba') is True
    assert solve('abca') is True


def test_corner_cases():
    assert solve('a') is True
    assert solve('') is True
    assert solve('aa') is True
    assert solve('ab') is True


def test_failure_cases():
    assert solve('abc') is False

from solution import Solution

solve = Solution().isPalindrome


def test_default():
    assert solve('A man, a plan, a canal: Panama') is True


def test_corner_cases():
    assert solve('') is True
    assert solve('a') is True
    assert solve('aa') is True


def test_failure_cases():
    assert solve('race a car') is False
    assert solve('ab') is False

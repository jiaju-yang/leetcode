from solution import Solution

solve = Solution().checkInclusion


def test_default():
    assert solve('ab', 'eidbaooo') is True


def test_corner_cases():
    assert solve('a', 'a') is True
    assert solve('', 'a') is True
    assert solve('', '') is True
    assert solve('a', '') is False
    assert solve('a', 'b') is False


def test_failure_cases():
    assert solve('ab', 'eidboaoo') is False

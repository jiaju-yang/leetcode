from solution import Solution

solve = Solution().minWindow


def test_default():
    assert solve('ADOBECODEBANC', 'ABC') == 'BANC'


def test_failure_cases():
    assert solve('a', '') == ''
    assert solve('', 'a') == ''
    assert solve('a', 'aa') == ''
    assert solve('', '') == ''


def test_corner_cases():
    assert solve('a', 'a') == 'a'
    assert solve('aa', 'a') == 'a'
    assert solve('aa', 'aa') == 'aa'

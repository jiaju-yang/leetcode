from solution import Solution

solve = Solution().minWindow


def test_default():
    assert solve('ADOBECODEBANC', 'ABC') == 'BANC'


def test_failure_cases():
    assert solve('ABAB', 'C') == ''
    assert solve('A', '') == ''
    assert solve('', 'A') == ''


def test_corner_cases():
    assert solve('AB', 'A') == 'A'
    assert solve('A', 'A') == 'A'
    assert solve('A', 'AA') == ''
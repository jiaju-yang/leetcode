from solution import Solution

solve = Solution().characterReplacement


def test_default():
    assert solve('ABAB', 2) == 4
    assert solve('AABABBA', 1) == 4
    assert solve('BAAAB', 2) == 5


def test_corner_cases():
    assert solve('A', 0) == 1
    assert solve('AB', 0) == 1
    assert solve('AB', 1) == 2
    assert solve('', 1) == 0
    assert solve('', 0) == 0

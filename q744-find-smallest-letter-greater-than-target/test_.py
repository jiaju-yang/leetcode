from solution import Solution

solve = Solution().nextGreatestLetter


def test_default():
    assert solve(['c', 'f', 'j'], 'a') == 'c'
    assert solve(['c', 'f', 'j'], 'c') == 'f'
    assert solve(['c', 'f', 'j'], 'd') == 'f'
    assert solve(['c', 'f', 'j'], 'g') == 'j'
    assert solve(['c', 'f', 'j'], 'j') == 'c'
    assert solve(['c', 'f', 'j'], 'k') == 'c'


def test_duplicate():
    assert solve(['e', 'e', 'e', 'e', 'e', 'e',
                  'n', 'n', 'n', 'n'], 'e') == 'n'

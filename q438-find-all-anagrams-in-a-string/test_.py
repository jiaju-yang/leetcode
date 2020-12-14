from solution import Solution

solve = Solution().findAnagrams


def test_default():
    assert solve('cbaebabacd', 'abc') == [0, 6]
    assert solve('abab', 'ab') == [0, 1, 2]


def test_corner_cases():
    assert solve('a', 'a') == [0]
    assert solve('', 'a') == []
    assert solve('aa', 'a') == [0, 1]

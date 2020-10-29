from solution import Solution

solve = Solution().lengthOfLongestSubstring


def test_default():
    assert solve('abcabcbb') == 3
    assert solve('pwwkew') == 3


def test_corner_cases():
    assert solve('bbbbb') == 1
    assert solve('b') == 1
    assert solve('') == 0

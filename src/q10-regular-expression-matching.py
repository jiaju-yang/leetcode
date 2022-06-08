#
# @lc app=leetcode id=10 lang=python3
#
# [10] Regular Expression Matching
#

# @lc code=start
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        if not p:
            return not s  # Brilliant base case check
        first_match = bool(s) and p[0] in (s[0], '.')
        if len(p) >= 2 and p[1] == '*':
            return self.isMatch(s, p[2:]) or (first_match and self.isMatch(s[1:], p))
        else:
            return first_match and self.isMatch(s[1:], p[1:])


# @lc code=end


solve = Solution().isMatch


def test_default():
    assert not solve('aa', 'a')
    assert solve('aa', 'a*')
    assert solve('abcd', 'a.*d')
    assert solve('ab', '.*')
    assert solve('aab', 'c*a*b')
    assert solve('aaa', 'ab*ac*a')
    assert solve('aasdfasdfasdfasdfas', 'aasdf.*asdf.*asdf.*asdf.*s')
    assert solve('baabbbaccbccacacc', 'c*..b*a*a.*a..*c')


def test_corner_cases():
    assert solve('a', 'a')
    assert not solve('a', 'b')
    assert solve('a', '.')
    assert solve('a', '.*')

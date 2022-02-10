#
# @lc app=leetcode id=394 lang=python3
#
# [394] Decode String
#

# @lc code=start


class Solution:
    def decodeString(self, s: str) -> str:
        if not s:
            return ''

        if s[0].isdigit():
            times, remain = s.split('[', 1)
            times = int(times)
            left_bracket_count = 1
            i = 0
            while left_bracket_count:
                if remain[i] == ']':
                    left_bracket_count -= 1
                elif remain[i] == '[':
                    left_bracket_count += 1
                i += 1
            return times * self.decodeString(remain[:i-1]) + self.decodeString(remain[i:])
        else:
            i = 0
            while i < len(s) and s[i].isalpha():
                i += 1
            return s[:i] + self.decodeString(s[i:])


# @lc code=end
solve = Solution().decodeString


def test_default():
    assert solve('3[a]2[bc]') == 'aaabcbc'
    assert solve('3[a2[c]]') == 'accaccacc'
    assert solve('2[abc]3[cd]ef') == 'abcabccdcdcdef'


def test_corner_cases():
    assert solve('a') == 'a'
    assert solve('2[a]') == 'aa'

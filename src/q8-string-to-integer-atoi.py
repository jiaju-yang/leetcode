#
# @lc app=leetcode id=8 lang=python3
#
# [8] String to Integer (atoi)
#

# @lc code=start
class Solution:
    int_max = 2**31-1
    int_min_abs = 2**31

    def myAtoi(self, s: str) -> int:
        s = s.strip()
        if not s:
            return 0
        negative = True if s[0] == '-' else False
        ret = 0
        start = 1 if s[0] == '+' or s[0] == '-' else 0
        for i in range(start, len(s)):
            if s[i].isdigit():
                if ret > self.int_max//10 or (ret == self.int_max//10 and int(s[i]) > (8 if negative else 7)):
                    ret = self.int_min_abs if negative else self.int_max
                    break
                ret = ret * 10 + int(s[i])
            else:
                break
        return -ret if negative else ret


# @lc code=end
solve = Solution().myAtoi


def test_default():
    assert solve('42') == 42
    assert solve('  -42') == -42
    assert solve('4193 with words') == 4193
    assert solve('words and 987') == 0


def test_corner_cases():
    assert solve('') == 0
    assert solve(' ') == 0
    assert solve(' +5') == 5
    assert solve(' -5') == -5
    assert solve('+2147483647') == 2147483647
    assert solve('+2147483648') == 2147483647
    assert solve('-2147483648') == -2147483648
    assert solve('-2147483649') == -2147483648

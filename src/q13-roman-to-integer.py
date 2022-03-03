#
# @lc app=leetcode id=13 lang=python3
#
# [13] Roman to Integer
#

# @lc code=start
class Solution:
    mapping = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }
    special = {
        'V': 'I',
        'X': 'I',
        'L': 'X',
        'C': 'X',
        'D': 'C',
        'M': 'C'
    }

    def romanToInt(self, s: str) -> int:
        previous = None
        ret = 0
        for c in s:
            if c in self.special and previous == self.special[c]:
                ret -= 2 * self.mapping[previous]
            ret += self.mapping[c]
            previous = c
        return ret


# @lc code=end
solve = Solution().romanToInt


def test_default():
    assert solve('III') == 3
    assert solve('LVIII') == 58
    assert solve('MCMXCIV') == 1994


def test_corner_cases():
    assert solve('I') == 1
    assert solve('IV') == 4
    assert solve('XC') == 90
    assert solve('CM') == 900

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

    def romanToInt(self, s: str) -> int:
        ret = 0
        for i in range(len(s) - 1):
            if self.mapping[s[i]] < self.mapping[s[i+1]]:
                ret -= self.mapping[s[i]]
            else:
                ret += self.mapping[s[i]]
        return ret + self.mapping[s[-1]]


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

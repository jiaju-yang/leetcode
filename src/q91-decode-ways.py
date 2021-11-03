#
# @lc app=leetcode id=91 lang=python3
#
# [91] Decode Ways
#

# @lc code=start
class Solution:
    def numDecodings(self, s: str) -> int:
        it = iter(s)
        p_char = next(it)
        previous, current = 1, (1 if self.is_valid(p_char) else 0)
        for c in it:
            previous, current, p_char = current, (
                current if self.is_valid(c) else 0) + (previous if self.is_valid(p_char + c) else 0), c
        return current

    def is_valid(self, t):
        if t.startswith('0'):
            return False
        return 1 <= int(t) <= 26
# @lc code=end


solve = Solution().numDecodings


def test_default():
    assert solve('11106') == 2
    assert solve('12') == 2
    assert solve('226') == 3


def test_corners():
    assert solve('0') == 0
    assert solve('06') == 0
    assert solve('6') == 1

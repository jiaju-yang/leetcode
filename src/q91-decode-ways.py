#
# @lc app=leetcode id=91 lang=python3
#
# [91] Decode Ways
#

# @lc code=start
class Solution:
    def __init__(self) -> None:
        self.valid = {str(i) for i in range(1, 27)}

    def numDecodings(self, s: str) -> int:
        if s.startswith('0'):
            return 0
        last, second_last = 1, 1
        for i in range(1, len(s)):
            cur = 0
            if s[i] in self.valid:
                cur += last
            if s[i-1:i+1] in self.valid:
                cur += second_last
            last, second_last = cur, last
        return last

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

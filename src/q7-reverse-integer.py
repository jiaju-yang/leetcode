#
# @lc app=leetcode id=7 lang=python3
#
# [7] Reverse Integer
#

# @lc code=start
class Solution:
    int_max = 2 ** 31 - 1
    int_min = -2 ** 31

    def reverse(self, x: int) -> int:
        if x >= 0:
            return self.reverse_positive(x)
        else:
            if x == self.int_min:
                return 0
            else:
                return -self.reverse_positive(-x)

    def reverse_positive(self, x):
        digits = []
        remain = x
        while remain != 0:
            remain, remainder = divmod(remain, 10)
            digits.append(remainder)

        ret = 0
        for d in digits:
            if ret > (self.int_max//10):
                return 0
            if ret == (self.int_max//10) and digits[0] > 7:
                return 0
            ret = (ret * 10 + d)
        return ret


# @lc code=end
solve = Solution().reverse


def test_default():
    assert solve(123) == 321
    assert solve(-123) == -321


def test_corner_cases():
    assert solve(120) == 21
    assert solve(0) == 0
    assert solve(2 ** 31-1) == 0
    assert solve(-2 ** 31) == 0
    assert solve(-2 ** 31+1) == 0

# #
# # @lc app=leetcode id=371 lang=python3
# #
# # [371] Sum of Two Integers
# #

# # @lc code=start
from itertools import zip_longest


class Solution:
    def getSum(self, a: int, b: int) -> int:
        mask = 0xfff
        max = 2047
        while b:
            a, b = (a ^ b) & mask, ((a & b) << 1) & mask
        return a if a <= max else ~(a ^ mask)

# # @lc code=end


solve = Solution().getSum


def test_default():
    assert solve(5, 2) == 7
    assert solve(0, 1000) == 1000


def test_overflow_cases():
    assert solve(1000, 1000) == 2000


def test_negative_cases():
    assert solve(-1, -2) == -3
    assert solve(-1, 2) == 1
    assert solve(-1, 1) == 0
    assert solve(-1, 0) == -1

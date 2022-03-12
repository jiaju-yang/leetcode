#
# @lc app=leetcode id=50 lang=python3
#
# [50] Pow(x, n)
#
import pytest

# @lc code=start


class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        if n < 0:
            return 1/self.myPow(x, -n)
        if n % 2 == 0:
            ret = self.myPow(x, n / 2)
            return ret * ret
        return x * self.myPow(x, n - 1)
# @lc code=end


solve = Solution().myPow


def test_default():
    assert solve(2, 10) == 1024
    assert solve(2.1, 3) == pytest.approx(9.261)
    assert solve(2, -2) == pytest.approx(0.25)


def test_corner_cases():
    assert solve(0, 0) == 1
    assert solve(0, 5) == 0
    assert solve(3, 0) == 1
    assert solve(3, 1) == 3
    assert solve(3, 2) == 9
    assert solve(-3, 2) == 9
    assert solve(-3, 1) == -3
    assert solve(-3, 0) == 1
    assert solve(3, -1) == pytest.approx(1/3)
    assert solve(3, -2) == pytest.approx(1/9)
    assert solve(-3, -1) == pytest.approx(-1/3)
    assert solve(-3, -2) == pytest.approx(1/9)

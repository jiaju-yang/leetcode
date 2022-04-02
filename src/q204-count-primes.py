#
# @lc app=leetcode id=204 lang=python3
#
# [204] Count Primes
#

# @lc code=start
from math import sqrt


class Solution:
    def countPrimes(self, n: int) -> int:
        if n < 3:
            return 0
        square_root = int(sqrt(n)) + 1
        numbers = [True] * n
        numbers[0] = numbers[1] = False
        for i in range(2, square_root):
            if numbers[i]:
                for j in range(i * i, n, i):
                    numbers[j] = False
        return sum(numbers)


# @lc code=end
solve = Solution().countPrimes


def test_default():
    assert solve(10) == 4


def test_corner_cases():
    assert solve(0) == 0
    assert solve(1) == 0
    assert solve(2) == 0
    assert solve(3) == 1
    assert solve(13) == 5

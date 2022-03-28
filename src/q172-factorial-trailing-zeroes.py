#
# @lc app=leetcode id=172 lang=python3
#
# [172] Factorial Trailing Zeroes
#


class RecursiveSolution:
    def trailingZeroes(self, n: int) -> int:
        return 0 if n == 0 else n // 5 + self.trailingZeroes(n // 5)

# @lc code=start


class Solution:
    def trailingZeroes(self, n: int) -> int:
        count = 0
        while n != 0:
            n //= 5
            count += n
        return count


# @lc code=end
solve = Solution().trailingZeroes


def test_default():
    assert solve(5) == 1
    assert solve(10) == 2
    assert solve(11) == 2
    assert solve(25) == 6


def test_corner_cases():
    assert solve(0) == 0
    assert solve(1) == 0
    assert solve(4) == 0

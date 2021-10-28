#
# @lc app=leetcode id=70 lang=python3
#
# [70] Climbing Stairs
#

# @lc code=start
class Solution:
    def climbStairs(self, n: int) -> int:
        a, b = 1, 1
        for i in range(n-1):
            a, b = b, a+b
        return b
# @lc code=end


solve = Solution().climbStairs


def test_default():
    assert solve(2) == 2
    assert solve(3) == 3
    assert solve(4) == 5


def test_corner_cases():
    assert solve(1) == 1

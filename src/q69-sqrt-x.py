#
# @lc app=leetcode id=69 lang=python3
#
# [69] Sqrt(x)
#

# @lc code=start
class Solution:
    def mySqrt(self, x: int) -> int:
        if not x:
            return 0
        prev = x
        while True:
            cur = prev / 2 + x / (2 * prev)
            if int(prev * 10) == int(cur * 10):
                return int(prev)
            prev = cur


# @lc code=end
solve = Solution().mySqrt


def test_default():
    assert solve(4) == 2
    assert solve(8) == 2
    assert solve(100) == 10
    assert solve(101) == 10
    assert solve(110) == 10


def test_corner_cases():
    assert solve(0) == 0
    assert solve(1) == 1
    assert solve(2) == 1
    assert solve(3) == 1
    assert solve(5) == 2

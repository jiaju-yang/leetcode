#
# @lc app=leetcode id=96 lang=python3
#
# [96] Unique Binary Search Trees
#

# @lc code=start
class Solution:
    def numTrees(self, n: int) -> int:
        dp = [1] * (n + 1)
        for i in range(2, n+1):
            dp[i] = sum(dp[j] * dp[i-j-1] for j in range(i))
        return dp[-1]


# @lc code=end
solve = Solution().numTrees


def test_default():
    assert solve(3) == 5


def test_corner_cases():
    assert solve(1) == 1

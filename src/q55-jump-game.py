#
# @lc app=leetcode id=55 lang=python3
#
# [55] Jump Game
#
from typing import List

# @lc code=start


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        dp = [False] * len(nums)
        dp[0] = True
        for i in range(1, len(nums)):
            for j in range(i-1, -1, -1):
                if dp[j] and i-j <= nums[j]:
                    dp[i] = True
                    break
        return dp[-1]
# @lc code=end


solve = Solution().canJump


def test_default():
    assert solve([2, 3, 1, 1, 4])
    assert not solve([3, 2, 1, 0, 4])


def test_corner_cases():
    assert solve([1])
    assert solve([0])
    assert not solve([0, 1])
    assert not solve([0, 2, 3])

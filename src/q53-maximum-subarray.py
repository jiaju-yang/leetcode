#
# @lc app=leetcode id=53 lang=python3
#
# [53] Maximum Subarray
#
from typing import List

# @lc code=start


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum, max_so_far = float('-inf'), 0
        for num in nums:
            max_sum = max(max_sum, num + max_so_far)
            max_so_far = max(0, num + max_so_far)
        return max_sum


# @lc code=end
solve = Solution().maxSubArray


def test_default():
    assert solve([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == 6
    assert solve([5, 4, -1, 7, 8]) == 23


def test_corner_cases():
    assert solve([1]) == 1
    assert solve([-1]) == -1
    assert solve([0]) == 0
    assert solve([2, -1]) == 2
    assert solve([-1, -2]) == -1

#
# @lc app=leetcode id=560 lang=python3
#
# [560] Subarray Sum Equals K
#
from typing import List

# @lc code=start


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        for i in range(len(nums)):
            current_sum = 0
            for j in range(i, len(nums)):
                current_sum += nums[j]
                if current_sum == k:
                    count += 1
        return count


# @lc code=end
solve = Solution().subarraySum


def test_default():
    assert solve([1, 1, 1], 2) == 2
    assert solve([1, 2, 3], 3) == 2


def test_corner_cases():
    assert solve([1], 1) == 1
    assert solve([1], 0) == 0
    assert solve([-1], 1) == 0
    assert solve([-1, -1], -1) == 2

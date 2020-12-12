#
# @lc app=leetcode id=209 lang=python3
#
# [209] Minimum Size Subarray Sum
#

# @lc code=start
from typing import List


class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        min_length = float('inf')
        current_sum = 0
        start = 0
        for i in range(len(nums)):
            current_sum += nums[i]
            while current_sum >= s:
                min_length = min(i-start+1, min_length)
                current_sum -= nums[start]
                start += 1
        return 0 if min_length == float('inf') else min_length


# @lc code=end

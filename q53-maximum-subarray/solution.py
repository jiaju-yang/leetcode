#
# @lc app=leetcode id=53 lang=python3
#
# [53] Maximum Subarray
#

# @lc code=start
from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maximum = nums[0]
        sum_so_far = max(0, nums[0])
        for i in range(1, len(nums)):
            current = nums[i] + sum_so_far
            if current > maximum:
                maximum = current
            sum_so_far = max(0, current)
        return maximum
        
# @lc code=end


#
# @lc app=leetcode id=16 lang=python3
#
# [16] 3Sum Closest
#

# @lc code=start
from typing import List


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        result = float('inf')
        for i in range(len(nums)-2):
            start, end = i+1, len(nums)-1
            while start < end:
                curr_sum = nums[i] + nums[start] + nums[end]
                if curr_sum == target:
                    return curr_sum
                elif curr_sum < target:
                    start += 1
                else:
                    end -= 1
                if abs(curr_sum-target) < abs(result-target):
                    result = curr_sum
        return result
# @lc code=end

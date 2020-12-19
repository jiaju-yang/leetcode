#
# @lc app=leetcode id=15 lang=python3
#
# [15] 3Sum
#

# @lc code=start
from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []
        for target_i in range(len(nums)-2):
            if nums[target_i] > 0:
                break
            if target_i > 0 and nums[target_i] == nums[target_i - 1]:
                continue
            target = -nums[target_i]
            start, end = target_i + 1, len(nums) - 1
            while start < end:
                curr_sum = nums[start] + nums[end]
                if curr_sum == target and start != target_i and end != target_i:
                    result.append([-target, nums[start], nums[end]])
                    start += 1
                    end -= 1
                    while start < end and nums[start] == nums[start-1]:
                        start += 1
                    while start < end and nums[end] == nums[end+1]:
                        end -= 1
                elif curr_sum < target:
                    start += 1
                else:
                    end -= 1
        return result

# @lc code=end

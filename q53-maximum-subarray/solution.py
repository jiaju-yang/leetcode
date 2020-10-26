#
# @lc app=leetcode id=53 lang=python3
#
# [53] Maximum Subarray
#
# @lc code=start
from typing import List


class DPSolution:
    def maxSubArray(self, nums: List[int]) -> int:
        maximum = nums[0]
        n = len(nums)
        sums = [[None for j in range(i, n)] for i in range(n)]
        for i in range(n):
            sums[i][0] = nums[i]
            if nums[i] > maximum:
                maximum = nums[i]
            for j in range(i+1, n):
                current = sums[i][j-1-i] + nums[j]
                if current > maximum:
                    maximum = current
                sums[i][j-i] = current
        return maximum


class OptimalDPSolution:
    def maxSubArray(self, nums: List[int]) -> int:
        maximum = nums[0]
        previous_max_suffix_sum = max(0, nums[0])
        for i in range(1, len(nums)):
            current_max_suffix_sum = max(
                nums[i] + previous_max_suffix_sum, nums[i])
            if current_max_suffix_sum > maximum:
                maximum = current_max_suffix_sum
            previous_max_suffix_sum = current_max_suffix_sum
        return maximum
# @lc code=end

#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#

# @lc code=start
from typing import List


class OptimalSolution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        complements = {}
        for i, num in enumerate(nums):
            if num in complements:
                return [complements[num], i]
            complements[target-num] = i
        return


class TwoPointersSolution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sorted_nums = sorted((num, i) for i, num in enumerate(nums))
        start, end = 0, len(sorted_nums) - 1
        while start < end:
            curr_sum = sorted_nums[start][0] + sorted_nums[end][0]
            if curr_sum == target:
                return [sorted_nums[start][1], sorted_nums[end][1]]
            elif curr_sum < target:
                start += 1
            else:
                end -= 1
        return


Solution = TwoPointersSolution
# @lc code=end

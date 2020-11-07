#
# @lc app=leetcode id=268 lang=python3
#
# [268] Missing Number
#
# @lc code=start
from typing import List


class SwapSolution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.append(None)
        none_position = len(nums) - 1
        for i in range(len(nums)):
            while nums[i] is not None and i != nums[i]:
                swap_index = nums[i]
                nums[i], nums[swap_index] = nums[swap_index], nums[i]
            if nums[i] is None:
                none_position = i
        return none_position


class XorSolution:
    def missingNumber(self, nums: List[int]) -> int:
        xor = len(nums)
        for i, num in enumerate(nums):
            xor ^= i ^ num
        return xor


Solution = XorSolution
# @lc code=end

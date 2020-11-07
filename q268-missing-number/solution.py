#
# @lc app=leetcode id=268 lang=python3
#
# [268] Missing Number
#

# @lc code=start
from typing import List


class Solution:
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
# @lc code=end

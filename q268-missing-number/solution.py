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
        for i in range(len(nums)):
            while nums[i] is not None and i != nums[i]:
                swap_index = nums[i]
                nums[i], nums[swap_index] = nums[swap_index], nums[i]
        for i in range(len(nums)):
            if nums[i] is None:
                return i


# @lc code=end

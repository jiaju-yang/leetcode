#
# @lc app=leetcode id=442 lang=python3
#
# [442] Find All Duplicates in an Array
#

# @lc code=start
from typing import List


class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        i = 0
        result = []
        while i < len(nums):
            target_i = nums[i]-1
            if nums[i] and nums[i] != i+1:
                if nums[target_i] == nums[i]:
                    result.append(nums[target_i])
                    nums[i] = 0
                else:
                    nums[target_i], nums[i] = nums[i], nums[target_i]
            else:
                i += 1
        return result

# @lc code=end

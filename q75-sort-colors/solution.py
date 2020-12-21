#
# @lc app=leetcode id=75 lang=python3
#
# [75] Sort Colors
#

# @lc code=start
from typing import List


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        i, j, k = 0, 0, 0
        while k < len(nums):
            if nums[k] == 1:
                nums[j], nums[k] = nums[k], nums[j]
                j += 1
            if nums[k] == 0:
                nums[i], nums[j] = nums[j], nums[i]
                if j != k:
                    nums[i], nums[k] = nums[k], nums[i]
                i += 1
                j += 1
            k += 1
        return

# @lc code=end

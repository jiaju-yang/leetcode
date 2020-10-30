#
# @lc app=leetcode id=26 lang=python3
#
# [26] Remove Duplicates from Sorted Array
#

# @lc code=start
from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i, j = 0, 1
        while j < len(nums):
            if nums[j] > nums[i]:
                i += 1
                nums[i] = nums[j]
            j += 1
        for _ in range(j-i-1):
            nums.pop()
        return len(nums)

# @lc code=end


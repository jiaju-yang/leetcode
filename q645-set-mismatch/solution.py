#
# @lc app=leetcode id=645 lang=python3
#
# [645] Set Mismatch
#

# @lc code=start
from typing import List


class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        result = [0, 0]
        for num in nums:
            if nums[abs(num)-1] > 0:
                nums[abs(num)-1] *= -1
            else:
                result[0] = abs(num)
        for i, num in enumerate(nums):
            if num > 0:
                result[1] = i+1
        return result

# @lc code=end

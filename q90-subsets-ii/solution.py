#
# @lc app=leetcode id=90 lang=python3
#
# [90] Subsets II
#
# @lc code=start
from typing import List


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = [[]]
        last_appended = None
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                last_appended = [item + [nums[i]] for item in last_appended]
            else:
                last_appended = [previous + [nums[i]] for previous in result]
            result.extend(last_appended)
        return result
# @lc code=end

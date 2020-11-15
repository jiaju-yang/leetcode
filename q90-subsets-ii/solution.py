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
        precious_size = len(result)
        for i in range(len(nums)):
            if i == 0 or nums[i] != nums[i-1]:
                precious_size = len(result)
            for j in range(len(result) - precious_size, len(result)):
                result.append(result[j] + [nums[i]])
        return result
# @lc code=end

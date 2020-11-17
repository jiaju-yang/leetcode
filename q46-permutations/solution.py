#
# @lc app=leetcode id=46 lang=python3
#
# [46] Permutations
#

# @lc code=start
from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 1:
            return [nums]
        result = []
        for i in range(len(nums)):
            sub_nums = nums[:]
            sub_nums.pop(i)
            sub_permutations = self.permute(sub_nums)
            for p in sub_permutations:
                result.append([nums[i]] + p)
        return result
# @lc code=end


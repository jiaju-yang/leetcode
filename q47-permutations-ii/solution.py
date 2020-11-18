#
# @lc app=leetcode id=47 lang=python3
#
# [47] Permutations II
#

# @lc code=start
from typing import List


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 1:
            return [nums]
        nums.sort()
        result = [[nums[0]]]
        for i in range(1, len(nums)):
            if nums[i] != nums[i-1]:
                result = [pre_perm[:j] + [nums[i]] + pre_perm[j:]
                          for pre_perm in result
                          for j in range(1 + len(pre_perm))]
            else:
                result = [pre_perm[:j] + [nums[i]] + pre_perm[j:]
                          for pre_perm in result
                          for j in range(1 + pre_perm.index(nums[i]))]
        return result
# @lc code=end

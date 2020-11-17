#
# @lc app=leetcode id=46 lang=python3
#
# [46] Permutations
#

# @lc code=start
from typing import List


class RecursiveSolution:
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


class IterativeSolution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = [[]]
        for i in range(len(nums)):
            new_result = []
            for pre_perm in result:
                for j in range(len(pre_perm) + 1):
                    perm = pre_perm[:]
                    perm.insert(j, nums[i])
                    new_result.append(perm)
            result = new_result
        return result


Solution = IterativeSolution
# @lc code=end

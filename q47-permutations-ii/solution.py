#
# @lc app=leetcode id=47 lang=python3
#
# [47] Permutations II
#

# @lc code=start
from typing import List
from collections import Counter


class IterativeSolution:
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


class BackTrackSolution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        def back_track(curr):
            if len(curr) == len(nums):
                result.append(curr[:])
                return
            for num, remain in counter.items():
                if remain > 0:
                    curr.append(num)
                    counter[num] -= 1
                    back_track(curr)
                    curr.pop()
                    counter[num] += 1

        counter = Counter(nums)
        result = []
        back_track([])
        return result


Solution = BackTrackSolution
# @lc code=end

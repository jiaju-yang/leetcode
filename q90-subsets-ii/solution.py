#
# @lc app=leetcode id=90 lang=python3
#
# [90] Subsets II
#
# @lc code=start
from typing import List


class IterativeSolution:
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


class BackTrackSolution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        def back_track(start, curr, target_length):
            if len(curr) == target_length:
                result.append(curr[:])
                return
            for j in range(start, len(nums)):
                if j > start and nums[j] == nums[j-1]:
                    continue
                curr.append(nums[j])
                back_track(j + 1, curr, target_length)
                curr.pop()
        result = []
        for i in range(len(nums) + 1):
            back_track(0, [], i)
        return result


Solution = BackTrackSolution
# @lc code=end

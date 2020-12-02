#
# @lc app=leetcode id=416 lang=python3
#
# [416] Partition Equal Subset Sum
#

# @lc code=start
from typing import List


class BruteForceSolution:
    def canPartition(self, nums: List[int]) -> bool:

        def driver(sub_nums):
            if len(sub_nums) == 1:
                return [[[sub_nums[0]], []]]
            result = []
            for comb in driver(sub_nums[1:]):
                result.append([comb[0] + [sub_nums[0]], comb[1]])
                result.append([comb[0], comb[1] + [sub_nums[0]]])
            return result
        total_sum = sum(nums)
        combs = driver(nums)
        for comb in combs:
            left_sum = sum(comb[0])
            if left_sum == total_sum - left_sum:
                return True
        return False


Solution = BruteForceSolution
# @lc code=end

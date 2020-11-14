#
# @lc app=leetcode id=78 lang=python3
#
# [78] Subsets
#
# @lc code=start
from typing import List


class BitsSolution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        n = len(nums)
        for i in range(2**n, 2**(n+1)):
            result.append([nums[p]
                           for p, b in enumerate(bin(i)[3:]) if b == '1'])
        return result


class RecursiveSolution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 1:
            return [[], [nums[0]]]
        subsets = self.subsets(nums[1:])
        result = []
        for i in subsets:
            result.append(i)
            result.append(list(i) + [nums[0]])
        return result


class IterativeSolution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = [[]]
        for num in nums:
            result.extend([previous + [num] for previous in result])
        return result


Solution = BitsSolution
# @lc code=end

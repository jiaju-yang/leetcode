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
            result.append(i + [nums[0]])
        return result


class IterativeSolution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = [[]]
        for num in nums:
            result.extend([previous + [num] for previous in result])
        return result


class BackTrackSolution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def back_track(start, curr, target_length):
            if len(curr) == target_length:
                result.append(curr[:])
                return
            curr.append(nums[start])
            back_track(start + 1, curr, target_length)
            curr.pop()
            back_track(start + 1, curr, target_length - 1)
        result = []
        back_track(0, [], len(nums))
        return result


class RealBackTrackSolution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def back_track(curr, start, target_length):
            if len(curr) == target_length:
                result.append(curr[:])
                return
            for j in range(start, len(nums)):
                curr.append(nums[j])
                back_track(curr, j + 1, target_length)
                curr.pop()
        result = []
        for i in range(len(nums)+1):
            back_track([], 0, i)
        return result


Solution = RealBackTrackSolution
# @lc code=end

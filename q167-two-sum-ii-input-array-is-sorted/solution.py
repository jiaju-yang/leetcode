#
# @lc app=leetcode id=167 lang=python3
#
# [167] Two Sum II - Input array is sorted
#
# @lc code=start
from typing import List


class TwoPointerSolution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        start, end = 0, len(numbers) - 1
        while start < end:
            the_sum = numbers[start] + numbers[end]
            if the_sum == target:
                return [start+1, end+1]
            elif the_sum > target:
                end -= 1
            else:
                start += 1
        return Nonex


class DictSolution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        complements = {}
        for i, number in enumerate(numbers):
            if number in complements:
                return [complements[number]+1, i + 1]
            complements[target-number] = i


Solution = DictSolution
# @lc code=end

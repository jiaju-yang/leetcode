#
# @lc app=leetcode id=448 lang=python3
#
# [448] Find All Numbers Disappeared in an Array
#

# @lc code=start
from typing import List


class SwapSolution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        i = 0
        while i < len(nums):
            num = nums[i]
            if num:
                if i+1 == num:
                    i += 1
                elif nums[num-1] == num:
                    nums[i] = None
                    i += 1
                else:
                    nums[num-1], nums[i] = nums[i], nums[num-1]
            else:
                i += 1
        return [i+1 for i, num in enumerate(nums) if num is None]


class HashSolution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        for i, num in enumerate(nums):
            if nums[abs(num)-1] > 0:
                nums[abs(num)-1] *= -1
        return [i+1 for i, num in enumerate(nums) if num > 0]


Solution = HashSolution
# @lc code=end

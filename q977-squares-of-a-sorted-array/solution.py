#
# @lc app=leetcode id=977 lang=python3
#
# [977] Squares of a Sorted Array
#

# @lc code=start
from typing import List


class TwoPointersSolution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        first_nonneg = 0
        while first_nonneg < len(nums):
            if nums[first_nonneg] >= 0:
                break
            first_nonneg += 1
        left, right = first_nonneg-1, first_nonneg
        result = []
        while left >= 0 and right < len(nums):
            if abs(nums[left]) < abs(nums[right]):
                result.append(nums[left]**2)
                left -= 1
            else:
                result.append(nums[right]**2)
                right += 1
        while left >= 0:
            result.append(nums[left]**2)
            left -= 1
        while right < len(nums):
            result.append(nums[right]**2)
            right += 1
        return result


class AnotherTwoPointersSolution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        result = [0] * len(nums)
        left, right = 0, len(nums)-1
        while left <= right:
            if abs(nums[left]) > abs(nums[right]):
                result[right - left] = nums[left]**2
                left += 1
            else:
                result[right - left] = nums[right]**2
                right -= 1
        return result


Solution = AnotherTwoPointersSolution
# @lc code=end

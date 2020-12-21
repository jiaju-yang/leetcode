#
# @lc app=leetcode id=75 lang=python3
#
# [75] Sort Colors
#

# @lc code=start
from typing import List


class TwoPointersSolution:
    def sortColors(self, nums: List[int]) -> None:
        i, j, k = 0, 0, 0
        while k < len(nums):
            if nums[k] == 1:
                nums[j], nums[k] = nums[k], nums[j]
                j += 1
            if nums[k] == 0:
                nums[i], nums[j] = nums[j], nums[i]
                if j != k:
                    nums[i], nums[k] = nums[k], nums[i]
                i += 1
                j += 1
            k += 1
        return


class AnotherTwoPointersSolution:
    def sortColors(self, nums: List[int]) -> None:
        i, j, k = 0, 0, len(nums) - 1
        while j <= k:
            if nums[j] == 0:
                nums[j], nums[i] = nums[i], nums[j]
                i += 1
                j += 1
            elif nums[j] == 2:
                nums[j], nums[k] = nums[k], nums[j]
                k -= 1
            else:
                j += 1
        return


Solution = AnotherTwoPointersSolution
# @lc code=end

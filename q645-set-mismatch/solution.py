#
# @lc app=leetcode id=645 lang=python3
#
# [645] Set Mismatch
#

# @lc code=start
from typing import List


class HashSolution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        result = [0, 0]
        for num in nums:
            if nums[abs(num)-1] > 0:
                nums[abs(num)-1] *= -1
            else:
                result[0] = abs(num)
        for i, num in enumerate(nums):
            if num > 0:
                result[1] = i+1
        return result


class XorSolution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        missing_xor_duplicate = 0
        for i, num in enumerate(nums, 1):
            missing_xor_duplicate ^= i
            missing_xor_duplicate ^= num
        right_most_bit_num = missing_xor_duplicate & -missing_xor_duplicate
        xor1, xor2 = 0, 0
        for i, num in enumerate(nums, 1):
            if num & right_most_bit_num == 0:
                xor1 ^= num
            else:
                xor2 ^= num
            if i & right_most_bit_num == 0:
                xor1 ^= i
            else:
                xor2 ^= i
        for num in nums:
            if num == xor1:
                return [xor1, xor2]
            if num == xor2:
                return [xor2, xor1]


Solution = XorSolution
# @lc code=end

#
# @lc app=leetcode id=260 lang=python3
#
# [260] Single Number III
#

# @lc code=start
from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        bit_mask = 0
        for num in nums:
            bit_mask ^= num
        diff = bit_mask & -bit_mask
        a = 0
        for num in nums:
            if num & diff:
                a ^= num
        return [a, bit_mask ^ a]
# @lc code=end

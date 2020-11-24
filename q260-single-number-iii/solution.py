#
# @lc app=leetcode id=260 lang=python3
#
# [260] Single Number III
#

# @lc code=start
from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        group = 0
        for num in nums:
            group ^= num
        i = 0
        while group % 2 == 0:
            i += 1
            group >>= 1
        pivot = 1 << i
        a, b = 0, 0
        for num in nums:
            if num & pivot:
                a ^= num
            else:
                b ^= num
        return [a, b]
# @lc code=end

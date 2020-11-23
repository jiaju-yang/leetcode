#
# @lc app=leetcode id=137 lang=python3
#
# [137] Single Number II
#

# @lc code=start
from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        a = b = 0
        for num in nums:
            temp = a
            a = (a & ~b & ~num) | (~a & b & num)
            b = (b & ~temp & ~num) | (~b & ~temp & num)
        return b
# @lc code=end

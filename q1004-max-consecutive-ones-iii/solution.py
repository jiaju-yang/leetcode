#
# @lc app=leetcode id=1004 lang=python3
#
# [1004] Max Consecutive Ones III
#

# @lc code=start
from typing import List


class Solution:
    def longestOnes(self, A: List[int], K: int) -> int:
        start = 0
        remain = K
        for end, value in enumerate(A):
            remain -= (1 - value)
            if remain < 0:
                remain += (1 - A[start])
                start += 1
        return end - start + 1

# @lc code=end

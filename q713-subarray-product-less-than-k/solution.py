#
# @lc app=leetcode id=713 lang=python3
#
# [713] Subarray Product Less Than K
#

# @lc code=start
from typing import List


class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        start, end = 0, 0
        curr_prod = 1
        count = 0
        for end, num in enumerate(nums):
            curr_prod *= num
            while curr_prod >= k and start <= end:
                curr_prod //= nums[start]
                start += 1
            count += end - start + 1
        return count

# @lc code=end

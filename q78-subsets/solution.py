#
# @lc app=leetcode id=78 lang=python3
#
# [78] Subsets
#

# @lc code=start
from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        for i in range(pow(2, len(nums))):
            item = []
            for p, c in enumerate(bin(i)[2:][::-1]):
                if c == '1':
                    item.append(nums[p])
            result.append(item)
        return result


# @lc code=end

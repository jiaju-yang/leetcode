#
# @lc app=leetcode id=11 lang=python3
#
# [11] Container With Most Water
#

# @lc code=start
from typing import List


class Solution:
    def maxArea(self, heights: List[int]) -> int:
        if len(heights) < 2:
            return 0
        left, right = 0, len(heights) - 1
        max_area = 0
        while left < right:
            if heights[left] < heights[right]:
                max_area = max(max_area, (right - left) * heights[left])
                left += 1
            else:
                max_area = max(max_area, (right - left) * heights[right])
                right -= 1
        return max_area

# @lc code=end

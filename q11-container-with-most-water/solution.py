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
        current_height = min(heights[left], heights[right])
        max_area = current_height * (right - left)
        while left < right:
            if heights[left] < heights[right]:
                new_left = left + 1
                while new_left < right and heights[new_left] <= heights[left]:
                    new_left += 1
                left = new_left
            else:
                new_right = right - 1
                while new_right > left and heights[new_right] <= heights[right]:
                    new_right -= 1
                right = new_right
            if left < right:
                max_area = max(
                    max_area, (right - left) * min(heights[left], heights[right]))
        return max_area

# @lc code=end

#
# @lc app=leetcode id=42 lang=python3
#
# [42] Trapping Rain Water
#

# @lc code=start
from typing import List


class FindHighestFirstSolution:
    def trap(self, heights: List[int]) -> int:
        highest = 0
        for i in range(1, len(heights)):
            if heights[i] > heights[highest]:
                highest = i

        traped_water = 0
        highest_left_so_far = 0
        for i in range(1, highest):
            water = heights[highest_left_so_far] - heights[i]
            if water > 0:
                traped_water += water
            else:
                highest_left_so_far = i

        highest_right_so_far = len(heights) - 1
        for i in range(highest_right_so_far, highest, -1):
            water = heights[highest_right_so_far] - heights[i]
            if water > 0:
                traped_water += water
            else:
                highest_right_so_far = i
        return traped_water


# @lc code=end

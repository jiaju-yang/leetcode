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


class StackSolution:
    def trap(self, heights: List[int]) -> int:
        traped_water = 0
        lefts = []
        lefts.append(0)
        right = 1
        while right < len(heights):
            if heights[lefts[-1]] < heights[right]:
                while len(lefts) > 1 and heights[lefts[-1]] < heights[right]:
                    bottom = lefts.pop()
                    left = lefts[-1]
                    traped_water += ((right - left - 1) *
                                     (min(heights[left], heights[right]) - heights[bottom]))
            while lefts and heights[right] >= heights[lefts[-1]]:
                lefts.pop()
            lefts.append(right)
            right += 1
        return traped_water


class TwoPointersSolution:
    def trap(self, heights: List[int]) -> int:
        highest_left, highest_right = 0, len(heights) - 1
        left, right = highest_left + 1, highest_right - 1
        traped_water = 0
        while left <= right:
            if heights[highest_left] < heights[highest_right]:
                if heights[left] < heights[highest_left]:
                    traped_water += heights[highest_left] - heights[left]
                else:
                    highest_left = left
                left += 1
            else:
                if heights[right] < heights[highest_right]:
                    traped_water += heights[highest_right] - heights[right]
                else:
                    highest_right = right
                right -= 1
        return traped_water


Solution = TwoPointersSolution
# @lc code=end

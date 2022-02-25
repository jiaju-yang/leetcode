#
# @lc app=leetcode id=84 lang=python3
#
# [84] Largest Rectangle in Histogram
#
from typing import List

# @lc code=start


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)

        left = [0] * n
        for i in range(n):
            j = i - 1
            while j >= 0 and heights[j] >= heights[i]:
                j = j - left[j] - 1
            left[i] = i - j - 1

        right = [0] * n
        for i in range(n - 1, -1, -1):
            j = i + 1
            while j < n and heights[j] >= heights[i]:
                j = j + right[j] + 1
            right[i] = j - i - 1

        return max((left[i] + right[i] + 1) * heights[i]
                   for i in range(n))


# @lc code=end
solve = Solution().largestRectangleArea


def test_default():
    assert solve([2, 1, 5, 6, 2, 3]) == 10
    assert solve([2, 4]) == 4


def test_corner_cases():
    assert solve([0]) == 0
    assert solve([1]) == 1
    assert solve([1, 0]) == 1
    assert solve([0, 1]) == 1

#
# @lc app=leetcode id=85 lang=python3
#
# [85] Maximal Rectangle
#
from typing import List

# @lc code=start


class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        heights = [0] * (len(matrix[0]) + 1)
        max_area = 0
        for row in matrix:
            for i in range(len(row)):
                heights[i] = (heights[i] + 1) if row[i] == '1' else 0
            stack = [-1]
            for i in range(len(heights)):
                while heights[i] < heights[stack[-1]]:
                    height = heights[stack.pop()]
                    width = i - stack[-1] - 1
                    max_area = max(max_area, height * width)
                stack.append(i)
        return max_area


# @lc code=end
solve = Solution().maximalRectangle


def test_default():
    assert solve([['1', '0', '1', '0', '0'], ['1', '0', '1', '1', '1'], [
                 '1', '1', '1', '1', '1'], ['1', '0', '0', '1', '0']]) == 6


def test_corner_cases():
    assert solve([['1']]) == 1
    assert solve([['0']]) == 0
    assert solve([['1', '1']]) == 2
    assert solve([['0', '1']]) == 1
    assert solve([['1', '0']]) == 1
    assert solve([['0', '0']]) == 0
    assert solve([['0'], ['1']]) == 1
    assert solve([['1'], ['1']]) == 2
    assert solve([['1'], ['0']]) == 1
    assert solve([['0'], ['0']]) == 0

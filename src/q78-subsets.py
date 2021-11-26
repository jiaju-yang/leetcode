#
# @lc app=leetcode id=78 lang=python3
#
# [78] Subsets
#
from typing import List

# @lc code=start


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = [[]]
        for num in nums:
            result = result + [previous + [num] for previous in result]
        return result
        result[:]

# @lc code=end


solve = Solution().subsets


def test_default():
    result = solve([1, 2, 3])
    assert len(result) == 8
    assert set(tuple(s) for s in result) == {
        tuple(), (1, ), (2, ), (1, 2), (3, ), (1, 3), (2, 3), (1, 2, 3)}


def test_corner_cases():
    result = solve([0])
    assert len(result) == 2
    assert set(tuple(s) for s in result) == {tuple(), (0, )}

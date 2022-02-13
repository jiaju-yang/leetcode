#
# @lc app=leetcode id=494 lang=python3
#
# [494] Target Sum
#
from typing import List

# @lc code=start


class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        it = iter(nums)
        first = next(it)
        combs = [first, -first]
        for num in it:
            combs = [comb + new_ele for comb in combs
                     for new_ele in (num, -num)]
        return sum(1 for comb in combs if comb == target)


# @lc code=end
solve = Solution().findTargetSumWays


def test_default():
    assert solve([1, 1, 1, 1, 1], 3) == 5


def test_corner_cases():
    assert solve([1], 1) == 1
    assert solve([1], 2) == 0
    assert solve([1], -1) == 1

#
# @lc app=leetcode id=494 lang=python3
#
# [494] Target Sum
#
from typing import List

# @lc code=start


class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        total = sum(nums)
        remaining = total
        max_remaining = []
        for num in nums:
            remaining -= num
            max_remaining.append(remaining)

        it = enumerate(nums)
        _, first = next(it)
        combs = [first, -first]
        for i, num in it:
            if num == 0:
                combs = combs + combs
                continue
            combs = [comb + new_ele
                     for comb in combs
                     for new_ele in (num, -num)
                     if -max_remaining[i] <= (comb + new_ele) - target <= max_remaining[i]]
        return sum(1 for comb in combs if comb == target)


# @lc code=end
solve = Solution().findTargetSumWays


def test_default():
    assert solve([1, 1, 1, 1, 1], 3) == 5
    assert solve([43, 9, 26, 24, 39, 40, 20, 11, 18, 13, 14,
                 30, 48, 47, 37, 24, 32, 32, 2, 26], 47) == 5844


def test_corner_cases():
    assert solve([1], 1) == 1
    assert solve([1], 2) == 0
    assert solve([1], -1) == 1
    assert solve([1, 0], 1) == 2

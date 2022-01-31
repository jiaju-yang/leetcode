#
# @lc app=leetcode id=169 lang=python3
#
# [169] Majority Element
#
from typing import List

# @lc code=start


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        it = iter(nums)
        potential, count = next(it), 1
        for num in it:
            if num == potential:
                count += 1
            elif count == 0:
                potential, count = num, 1
            else:
                count -= 1
        return potential


# @lc code=end
solve = Solution().majorityElement


def test_default():
    assert solve([3, 2, 3]) == 3
    assert solve([2, 2, 1, 1, 1, 2, 2]) == 2


def test_corner_cases():
    assert solve([1]) == 1
    assert solve([1, 1]) == 1
    assert solve([1, 2, 1]) == 1

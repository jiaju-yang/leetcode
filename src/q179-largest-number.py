#
# @lc app=leetcode id=179 lang=python3
#
# [179] Largest Number
#
from typing import List
from functools import cmp_to_key


# @lc code=start
class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        if not any(nums):
            return '0'
        return ''.join(sorted(map(str, nums), key=cmp_to_key(lambda a, b: int(b + a) - int(a + b))))


# @lc code=end
solve = Solution().largestNumber


def test_default():
    assert solve([10, 2]) == '210'
    assert solve([3, 30, 34, 5, 9]) == '9534330'


def test_corner_cases():
    assert solve([34, 3]) == "343"
    assert solve([3, 34]) == "343"
    assert solve([432, 43243]) == "43243432"
    assert solve([8308, 8308, 830]) == "83088308830"
    assert solve([0, 0]) == "0"

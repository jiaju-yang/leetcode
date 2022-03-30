#
# @lc app=leetcode id=179 lang=python3
#
# [179] Largest Number
#
from typing import List


# @lc code=start
class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        integers = sorted(Num(num) for num in nums)
        i = len(integers) - 1
        while i > 0:
            if integers[i].integer == '0':
                integers.pop()
            else:
                break
            i -= 1
        return ''.join(str(num) for num in integers[::-1])


class Num:
    def __init__(self, integer) -> None:
        self.integer = str(integer)

    def __lt__(self, other):
        i = 0
        length = min(len(self.integer), len(other.integer))
        while i < length:
            if int(self.integer[i]) != int(other.integer[i]):
                return int(self.integer[i]) < int(other.integer[i])
            i += 1
        if len(self.integer) < len(other.integer):
            return Num(other.integer[i:]) > self
        elif len(self.integer) == len(other.integer):
            return True
        return Num(self.integer[i:]) < other

    def __str__(self) -> str:
        return self.integer


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

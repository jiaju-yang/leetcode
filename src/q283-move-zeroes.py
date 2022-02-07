#
# @lc app=leetcode id=283 lang=python3
#
# [283] Move Zeroes
#
from typing import List

# @lc code=start


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        left, right = -1, 0
        while right < len(nums):
            if nums[right] != 0:
                left += 1
                nums[left], nums[right] = nums[right], nums[left]
            right += 1


# @lc code=end
solve = Solution().moveZeroes


def test_default():
    nums = [0, 1, 0, 3, 12]
    solve(nums)
    assert nums == [1, 3, 12, 0, 0]


def test_corner_cases():
    nums = [0]
    solve(nums)
    assert nums == [0]

    nums = [1]
    solve(nums)
    assert nums == [1]

    nums = [0, 1]
    solve(nums)
    assert nums == [1, 0]

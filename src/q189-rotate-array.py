#
# @lc app=leetcode id=189 lang=python3
#
# [189] Rotate Array
#
from typing import List

# @lc code=start


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        k = k % len(nums)
        if k > 0:
            nums[:] = nums[-k:] + nums[:len(nums)-k]


# @lc code=end
solve = Solution().rotate


def test_default():
    nums = [1, 2, 3, 4, 5, 6, 7]
    solve(nums, 3)
    assert nums == [5, 6, 7, 1, 2, 3, 4]

    nums = [-1, -100, 3, 99]
    solve(nums, 2)
    assert nums == [3, 99, -1, -100]


def test_corner_cases():
    nums = [1, 2]
    solve(nums, 3)
    assert nums == [2, 1]

    nums = [1]
    solve(nums, 3)
    assert nums == [1]

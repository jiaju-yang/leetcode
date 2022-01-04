#
# @lc app=leetcode id=31 lang=python3
#
# [31] Next Permutation
#
from typing import List

# @lc code=start


class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in range(len(nums)-1, 0, -1):
            if nums[i] > nums[i-1]:
                for j in range(len(nums)-1, i-1, -1):
                    if nums[j] > nums[i-1]:
                        break
                nums[i-1], nums[j] = nums[j], nums[i-1]
                nums[i:] = nums[:i-1:-1]
                return
        nums[:] = nums[::-1]
        return


# @lc code=end
solve = Solution().nextPermutation


def test_default():
    nums = [1, 2, 3]
    solve(nums)
    assert nums == [1, 3, 2]

    nums = [3, 2, 1]
    solve(nums)
    assert nums == [1, 2, 3]

    nums = [1, 1, 5]
    solve(nums)
    assert nums == [1, 5, 1]

    nums = [1, 3, 2]
    solve(nums)
    assert nums == [2, 1, 3]

    nums = [2, 3, 1]
    solve(nums)
    assert nums == [3, 1, 2]

    nums = [1, 4, 3, 2]
    solve(nums)
    assert nums == [2, 1, 3, 4]


def test_corner_cases():
    nums = [1]
    solve(nums)
    assert nums == [1]

    nums = [1, 2]
    solve(nums)
    assert nums == [2, 1]

    nums = [2, 1]
    solve(nums)
    assert nums == [1, 2]

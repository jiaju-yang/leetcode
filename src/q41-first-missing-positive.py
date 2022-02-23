#
# @lc app=leetcode id=41 lang=python3
#
# [41] First Missing Positive
#
from typing import List

# @lc code=start


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums.append(0)
        n = len(nums)
        for i in range(n):
            while n > nums[i] > 0 and nums[i] != i and nums[i] != nums[nums[i]]:
                temp = nums[i]
                nums[i] = nums[nums[i]]
                nums[temp] = temp
        i = 1
        while i < n:
            if nums[i] <= 0 or nums[i] >= n or nums[i] != i:
                return i
            i += 1
        return i


# @lc code=end
solve = Solution().firstMissingPositive


def test_default():
    assert solve([1, 2, 0]) == 3
    assert solve([3, 4, -1, 1]) == 2
    assert solve([7, 8, 9, 11, 12]) == 1


def test_corner_cases():
    assert solve([-1]) == 1
    assert solve([0]) == 1
    assert solve([1]) == 2
    assert solve([2]) == 1
    assert solve([1, 1]) == 2
    assert solve([2, 2]) == 1

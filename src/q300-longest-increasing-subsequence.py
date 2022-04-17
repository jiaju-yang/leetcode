#
# @lc app=leetcode id=300 lang=python3
#
# [300] Longest Increasing Subsequence
#
from typing import List


class DPSolution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [1] * len(nums)
        for i in range(1, len(nums)):
            dp[i] = max((dp[j] + 1 for j in range(i) if nums[j] < nums[i]),
                        default=dp[i])
        return max(dp)

# @lc code=start


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        l = [nums[0]]
        for i in range(1, len(nums)):
            if nums[i] > l[-1]:
                l.append(nums[i])
            else:
                index = self.binary_search(l, nums[i])
                if l[index] > nums[i]:
                    l[index] = nums[i]
        return len(l)

    def binary_search(self, l, target):
        i, j = 0, len(l) - 1
        while i <= j:
            middle = (i + j) >> 1
            if l[middle] == target:
                return middle
            elif l[middle] < target:
                i = middle + 1
            else:
                j = middle - 1
        return i
# @lc code=end


solve = Solution().lengthOfLIS


def test_default():
    assert solve([1, 3, 6, 7, 9, 4, 10, 5, 6]) == 6
    assert solve([10, 9, 2, 5, 3, 7, 101, 18]) == 4
    assert solve([0, 1, 0, 3, 2, 3]) == 4
    assert solve([7, 7, 7, 7, 7, 7, 7]) == 1


def test_corner_cases():
    assert solve([1]) == 1
    assert solve([1, 2]) == 2
    assert solve([-1, 2]) == 2
    assert solve([-1]) == 1

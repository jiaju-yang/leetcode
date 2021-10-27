#
# @lc app=leetcode id=416 lang=python3
#
# [416] Partition Equal Subset Sum
#
from typing import List


class DPSolution:
    def canPartition(self, nums: List[int]) -> bool:
        n = len(nums)
        differences = {0}
        for num in nums:
            new_differences = set()
            for d in differences:
                new_differences.add(d-num)
                new_differences.add(d+num)
            differences = new_differences
        if 0 in differences:
            return True
        return False

# @lc code=start


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if not nums:
            return True
        total = sum(nums)
        target = total >> 1
        if (target << 1) != total:
            return False
        dp = {0}
        for num in nums:
            dp.update({get+num for get in dp})
            if target in dp:
                return True
        return False


# @lc code=end
solve = Solution().canPartition


def test_default():
    assert solve([1, 5, 11, 5])
    assert not solve([1, 2, 3, 5])


def test_corner_cases():
    assert solve([])
    assert solve([0])
    assert not solve([1])
    assert solve([1, 1])
    assert not solve([1, 2])

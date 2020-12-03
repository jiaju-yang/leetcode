#
# @lc app=leetcode id=416 lang=python3
#
# [416] Partition Equal Subset Sum
#

# @lc code=start
from typing import List
from collections import Counter


class BruteForceSolution:
    def canPartition(self, nums: List[int]) -> bool:

        def driver(sub_nums):
            if len(sub_nums) == 1:
                return [[[sub_nums[0]], []]]
            result = []
            for comb in driver(sub_nums[1:]):
                result.append([comb[0] + [sub_nums[0]], comb[1]])
                result.append([comb[0], comb[1] + [sub_nums[0]]])
            return result
        total_sum = sum(nums)
        combs = driver(nums)
        for comb in combs:
            left_sum = sum(comb[0])
            if left_sum == total_sum - left_sum:
                return True
        return False


class ImprovedBruteForceSolution:
    def canPartition(self, nums: List[int]) -> bool:
        def is_sum(sub_sum, curr):
            if sub_sum == 0:
                return True
            if curr < 0 or sub_sum < 0:
                return False
            included = is_sum(sub_sum - nums[curr], curr - 1)
            not_included = is_sum(sub_sum, curr - 1)
            return included or not_included

        total_sum = sum(nums)
        if total_sum % 2 == 1:
            return False
        target = total_sum >> 1
        return is_sum(target, len(nums) - 1)


class BackTrackSolution:
    def canPartition(self, nums: List[int]) -> bool:
        total_sum = sum(nums)
        counter = Counter(nums)

        def driver(current_sum):
            if current_sum == total_sum - current_sum:
                return True
            if current_sum > total_sum - current_sum:
                return False
            for num, remain in counter.items():
                if remain > 0:
                    counter[num] -= 1
                    equal = driver(current_sum+num)
                    if equal:
                        return equal
                    counter[num] += 1
            return False
        return driver(0)


class DPSolution:
    def canPartition(self, nums: List[int]) -> bool:
        total_sum = sum(nums)
        if total_sum % 2 == 1:
            return False
        target = total_sum >> 1
        dp = [False] * (target + 1)
        dp[0] = True
        for num in nums:
            for i in range(target - num, -1, -1):
                if dp[i]:
                    dp[i+num] = True
            if dp[target]:
                return True
        return False


class AnotherDPSolution:
    def canPartition(self, nums: List[int]) -> bool:
        total_sum = sum(nums)
        if total_sum % 2 == 1:
            return False
        target = total_sum >> 1
        dp = [[False] * (target + 1) for _ in range(len(nums) + 1)]
        dp[0][0] = True
        for i in range(len(nums)):
            for sub_sum in range(target + 1):
                j = sub_sum - nums[i]
                if j >= 0 and dp[i][j]:
                    dp[i+1][sub_sum] = True
                if dp[i][sub_sum]:
                    dp[i+1][sub_sum] = True
        return dp[len(nums)][target]


Solution = DPSolution
# @lc code=end

#
# @lc app=leetcode id=128 lang=python3
#
# [128] Longest Consecutive Sequence
#
from typing import List


class DFSSolution:
    def longestConsecutive(self, nums: List[int]) -> int:
        states = {num: False for num in nums}
        max_length = 0
        for num in nums:
            if not states[num]:
                max_length = max(max_length, self.dfs(num, states))
        return max_length

    def dfs(self, num, states):
        states[num] = True
        length = 1
        for neighbor in self.neighbors(num):
            if not states.get(neighbor, True):
                length += self.dfs(neighbor, states)
        return length

    def neighbors(self, num):
        yield num + 1
        yield num - 1

# @lc code=start


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        longest = 0
        for num in nums:
            if num - 1 not in s:
                next = num + 1
                while next in s:
                    next += 1
                longest = max(longest, next - num)
        return longest


# @lc code=end


solve = Solution().longestConsecutive


def test_default():
    assert solve([100, 4, 200, 1, 3, 2]) == 4
    assert solve([0, 3, 7, 2, 5, 8, 4, 6, 0, 1]) == 9


def test_corner_cases():
    assert solve([1]) == 1
    assert solve([]) == 0
    assert solve([1, 2]) == 2
    assert solve([1, 3]) == 1
    assert solve([-1]) == 1
    assert solve([-1, -2]) == 2

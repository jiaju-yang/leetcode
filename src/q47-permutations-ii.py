#
# @lc app=leetcode id=47 lang=python3
#
# [47] Permutations II
#
from typing import List

# @lc code=start


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        sorted_nums = sorted(nums)
        it = iter(sorted_nums)
        result = [[next(it)]]
        for i, num in enumerate(it, start=1):
            if num == sorted_nums[i-1]:
                result = [perm[:j] + [num] + perm[j:]
                          for perm in result
                          for j in range(perm.index(num)+1)]
            else:
                result = [perm[:j] + [num] + perm[j:]
                          for perm in result
                          for j in range(len(perm)+1)]
        return result

# @lc code=end


solve = Solution().permuteUnique


def test_default():
    assert solve([1, 1, 2]) == [[2, 1, 1], [1, 2, 1], [1, 1, 2]]

    assert solve([1, 2, 3]) == [[3, 2, 1], [2, 3, 1], [
        2, 1, 3], [3, 1, 2], [1, 3, 2], [1, 2, 3]]


def test_corner_cases():
    assert solve([1]) == [[1]]
    assert solve([1, 2]) == [[2, 1], [1, 2]]
    assert solve([1, 1]) == [[1, 1]]
    assert solve([2, 2, 2, 2]) == [[2, 2, 2, 2]]

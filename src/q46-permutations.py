#
# @lc app=leetcode id=46 lang=python3
#
# [46] Permutations
#
from typing import List

# @lc code=start


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        it = iter(nums)
        result = [[next(it)]]
        for num in it:
            result = [perm[:i] + [num] + perm[i:]
                      for perm in result
                      for i in range(len(perm)+1)]
        return result


# @lc code=end
solve = Solution().permute


def test_default():
    assert solve([1, 2, 3]) == [[3, 2, 1], [2, 3, 1], [
        2, 1, 3], [3, 1, 2], [1, 3, 2], [1, 2, 3]]
    assert solve([0, 1]) == [[1, 0], [0, 1]]


def test_corner_cases():
    assert solve([1]) == [[1]]

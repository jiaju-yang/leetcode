#
# @lc app=leetcode id=39 lang=python3
#
# [39] Combination Sum
#
from typing import List

# @lc code=start


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ret = []
        self.dfs(sorted(candidates), target, [], ret)
        return ret

    def dfs(self, candidates, target, path, ret):
        if target == 0:
            ret.append(path)
            return
        if target < 0 or not candidates:
            return
        first, remain = candidates[0], candidates[1:]
        for i in range((target//first) + 1):
            self.dfs(remain, target - first * i, path + ([first] * i), ret)


# @lc code=end
solve = Solution().combinationSum


def test_default():
    assert solve([2, 3, 6, 7], 7) == [[7], [2, 2, 3]]
    assert solve([2, 3, 5], 8) == [[3, 5], [2, 3, 3], [2, 2, 2, 2]]


def test_corner_cases():
    assert solve([2], 1) == []
    assert solve([2], 2) == [[2]]
    assert solve([1, 2], 2) == [[2], [1, 1]]

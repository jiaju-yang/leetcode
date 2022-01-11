#
# @lc app=leetcode id=39 lang=python3
#
# [39] Combination Sum
#
from typing import List

# @lc code=start


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        return self.dfs(sorted(candidates), target)

    def dfs(self, remain_candidates, target):
        if not remain_candidates or target <= 0:
            return []
        first = remain_candidates[0]
        if target < first:
            return []
        result = []
        for used_times in range((target//first) + 1):
            remain_target = target - used_times * first
            if remain_target == 0:
                result.append([first] * used_times)
            else:
                result.extend(r + ([first] * used_times)
                              for r in self.dfs(remain_candidates[1:], remain_target))
        return result


# @lc code=end
solve = Solution().combinationSum


def test_default():
    assert solve([2, 3, 6, 7], 7) == [[7], [3, 2, 2]]
    assert solve([2, 3, 5], 8) == [[5, 3], [3, 3, 2], [2, 2, 2, 2]]


def test_corner_cases():
    assert solve([2], 1) == []
    assert solve([2], 2) == [[2]]
    assert solve([1, 2], 2) == [[2], [1, 1]]

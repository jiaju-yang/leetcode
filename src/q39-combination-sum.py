#
# @lc app=leetcode id=39 lang=python3
#
# [39] Combination Sum
#
from typing import List

# @lc code=start
from collections import defaultdict


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        dp = defaultdict(list)
        dp[0] = [[]]
        candidates = sorted(candidates)
        for sub_target in range(candidates[0], target + 1):
            for num in candidates:
                if dp[sub_target - num]:
                    potential = []
                    for comb in dp[sub_target - num]:
                        if comb and comb[-1] > num:
                            continue
                        potential.append(comb + [num])
                    dp[sub_target].extend(potential)
        return dp[target]


# @lc code=end
solve = Solution().combinationSum


def test_default():
    assert solve([2, 3, 6, 7], 7) == [[2, 2, 3], [7]]
    assert solve([2, 3, 5], 8) == [[2, 2, 2, 2], [2, 3, 3], [3, 5]]


def test_corner_cases():
    assert solve([2], 1) == []
    assert solve([2], 2) == [[2]]
    assert solve([1, 2], 2) == [[1, 1], [2]]

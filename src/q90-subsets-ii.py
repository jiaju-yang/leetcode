#
# @lc app=leetcode id=90 lang=python3
#
# [90] Subsets II
#
from typing import Counter, List

# @lc code=start


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        sorted_nums = sorted(nums)
        result = [[]]
        last_appended = []
        for i, num in enumerate(sorted_nums):
            if i > 0 and num == sorted_nums[i-1]:
                last_appended = [combination + [num]
                                 for combination in last_appended]
            else:
                last_appended = [combination + [num]
                                 for combination in result]
            result += last_appended

        return result
# @lc code=end


solve = Solution().subsetsWithDup


def test_default():
    result = solve([1, 2, 2])
    assert len(result) == 6
    assert set(tuple(s) for s in result) == {
        tuple(), (1, ), (2, ), (1, 2), (2, 2), (1, 2, 2)}

    result = solve([1, 2, 2, 2])
    assert len(result) == 8
    assert set(tuple(s) for s in result) == {
        tuple(), (1, ), (2, ), (1, 2), (2, 2), (1, 2, 2), (2, 2, 2), (1, 2, 2, 2)}


def test_corner_cases():
    result = solve([0])
    assert len(result) == 2
    assert set(tuple(s) for s in result) == {tuple(), (0, )}

    result = solve([5, 5, 5, 5, 5])
    assert len(result) == 6
    assert set(tuple(s) for s in result) == {
        tuple(), (5, ), (5, 5), (5, 5, 5), (5, 5, 5, 5), (5, 5, 5, 5, 5)}

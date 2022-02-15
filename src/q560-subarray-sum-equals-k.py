#
# @lc app=leetcode id=560 lang=python3
#
# [560] Subarray Sum Equals K
#
from collections import defaultdict
from typing import List

# @lc code=start


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        previous_sums = defaultdict(int)
        previous_sums[0] = 1
        cur_sum, count = 0, 0
        for num in nums:
            cur_sum += num
            count += previous_sums[cur_sum - k]
            previous_sums[cur_sum] += 1
        return count


# @lc code=end
solve = Solution().subarraySum


def test_default():
    assert solve([1, 1, 1], 2) == 2
    assert solve([1, 2, 3], 3) == 2


def test_corner_cases():
    assert solve([1], 1) == 1
    assert solve([1], 0) == 0
    assert solve([-1], 1) == 0
    assert solve([-1, -1], -1) == 2
    assert solve([0], 0) == 1
    assert solve([0, 0], 0) == 3

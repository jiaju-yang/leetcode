#
# @lc app=leetcode id=347 lang=python3
#
# [347] Top K Frequent Elements
#
from typing import List
from collections import Counter
from heapq import nlargest

# @lc code=start


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)
        return nlargest(k, counter.keys(), key=counter.get)

# @lc code=end


solve = Solution().topKFrequent


def test_default():
    assert set(solve([1, 1, 1, 2, 2, 3], 2)) == {1, 2}


def test_corner_cases():
    assert solve([1], 1) == [1]
    assert solve([1, 1, 2], 1) == [1]

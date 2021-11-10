#
# @lc app=leetcode id=347 lang=python3
#
# [347] Top K Frequent Elements
#
from typing import List
from collections import Counter
from heapq import heapify, heappushpop

# @lc code=start


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)
        it = iter(counter.items())
        heap = []
        for _ in range(k):
            k, v = next(it)
            heap.append((v, k))
        heapify(heap)
        for k, v in it:
            heappushpop(heap, (v, k))
        return [k for _, k in heap]

# @lc code=end


solve = Solution().topKFrequent


def test_default():
    assert set(solve([1, 1, 1, 2, 2, 3], 2)) == {1, 2}


def test_corner_cases():
    assert solve([1], 1) == [1]
    assert solve([1, 1, 2], 1) == [1]

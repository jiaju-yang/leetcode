#
# @lc app=leetcode id=347 lang=python3
#
# [347] Top K Frequent Elements
#
from typing import List
from collections import Counter
from heapq import nlargest
from random import randint


class HeapSolution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)
        return nlargest(k, counter.keys(), key=counter.get)

# @lc code=start


class QuickSelectSolution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)
        frequency = [(k, v) for k, v in counter.items()]
        self.quick_select(frequency, 0, len(frequency) -
                          1, k, key=lambda pair: pair[1])
        return [frequency[i][0] for i in range(k)]

    def quick_select(self, nums, start, end, k, key=lambda num: num):
        if start >= end:
            return
        pivot = randint(start, end)
        nums[pivot], nums[end] = nums[end], nums[pivot]
        i = start
        for j in range(start, end):
            if key(nums[j]) > key(nums[end]):
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
        nums[i], nums[end] = nums[end], nums[i]
        if i == k:
            return
        elif i < k:
            self.quick_select(nums, i + 1, end, k, key)
        else:
            self.quick_select(nums, start, i - 1, k, key)


Solution = QuickSelectSolution
# @lc code=end


solve = Solution().topKFrequent


def test_default():
    assert set(solve([1, 1, 1, 2, 2, 3], 2)) == {1, 2}


def test_corner_cases():
    assert solve([1], 1) == [1]
    assert solve([1, 1, 2], 1) == [1]

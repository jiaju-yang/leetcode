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
        frequency = list(counter.keys())
        self.quick_select(frequency, 0, len(frequency) - 1, k, key=counter.get)
        return frequency[:k]

    def quick_select(self, nums, start, end, k, key=lambda num: num):
        if start >= end:
            return
        pivot = self.partition(nums, start, end, k, key)
        if pivot == k:
            return
        elif pivot < k:
            self.quick_select(nums, pivot + 1, end, k, key)
        else:
            self.quick_select(nums, start, pivot - 1, k, key)

    def partition(self, nums, start, end, k, key):
        pivot = randint(start, end)
        nums[pivot], nums[end] = nums[end], nums[pivot]
        i = start
        for j in range(start, end):
            if key(nums[j]) > key(nums[end]):
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
        nums[i], nums[end] = nums[end], nums[i]
        return i


Solution = QuickSelectSolution
# @lc code=end


solve = Solution().topKFrequent


def test_default():
    assert set(solve([1, 1, 1, 2, 2, 3], 2)) == {1, 2}


def test_corner_cases():
    assert solve([1], 1) == [1]
    assert solve([1, 1, 2], 1) == [1]

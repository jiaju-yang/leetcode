#
# @lc app=leetcode id=215 lang=python3
#
# [215] Kth Largest Element in an Array
#

# @lc code=start
from typing import List
from random import choice
from heapq import heapify, heappop


class HeapSolution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = [-num for num in nums]
        heapify(heap)
        for _ in range(k-1):
            heappop(heap)
        return -heappop(heap)


class DivideAndConquerSolution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        partitioned = nums[:]
        while k != 1:
            pivot = choice(partitioned)
            larger = [num for num in partitioned if num >= pivot]
            smaller = [num for num in partitioned if num < pivot]
            if not larger and len(set(smaller)) == 1:
                return smaller[0]
            if not smaller and len(set(larger)) == 1:
                return larger[0]
            if len(larger) >= k:
                partitioned = larger
            else:
                partitioned = smaller
                k -= len(larger)
        return max(partitioned)


class InplaceDivideAndConquerSolution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        left, right = 0, len(nums) - 1
        return self._find(nums, left, right, k)

    def _find(self, nums, left, right, k):
        pivot_index = self._partition(nums, left, right)
        if pivot_index == k - 1:
            return nums[pivot_index]
        elif pivot_index < k - 1:
            return self._find(nums, pivot_index + 1, right, k)
        else:
            return self._find(nums, left, pivot_index - 1, k)

    def _partition(self, nums, p, r):
        pivot_index = choice(range(r - p + 1)) + p
        pivot = nums[pivot_index]
        nums[pivot_index], nums[r] = nums[r], nums[pivot_index]
        i = p
        for j in range(p, r):
            if nums[j] >= pivot:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
        nums[i], nums[r] = nums[r], nums[i]
        return i


Solution = InplaceDivideAndConquerSolution
# @lc code=end

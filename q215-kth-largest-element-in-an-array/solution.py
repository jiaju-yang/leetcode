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


Solution = DivideAndConquerSolution
# @lc code=end

#
# @lc app=leetcode id=215 lang=python3
#
# [215] Kth Largest Element in an Array
#

# @lc code=start
from typing import List
from heapq import heapify, heappop


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = [-num for num in nums]
        heapify(heap)
        for _ in range(k-1):
            heappop(heap)
        return -heappop(heap)


# @lc code=end

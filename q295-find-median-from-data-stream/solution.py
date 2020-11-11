#
# @lc app=leetcode id=295 lang=python3
#
# [295] Find Median from Data Stream
#

# @lc code=start
from heapq import heapify, heappush, heappop


class Heap:
    def __init__(self):
        self.data = []

    def insert(self, element):
        heappush(self.data, element)

    def __len__(self):
        return len(self.data)

    def extract(self):
        return heappop(self.data)

    def _top(self):
        return self.data[0]


class MinHeap(Heap):
    def min(self):
        return self._top()


class MaxHeap(Heap):
    def insert(self, element):
        heappush(self.data, -element)

    def max(self):
        return -self._top()

    def extract(self):
        return -super().extract()


class MedianFinder:

    def __init__(self):
        self.big_half = MinHeap()
        self.small_half = MaxHeap()

    def addNum(self, num: int) -> None:
        if len(self.big_half) == 0:
            self.big_half.insert(num)
        elif len(self.small_half) < len(self.big_half):
            if num > self.big_half.min():
                self.small_half.insert(self.big_half.extract())
                self.big_half.insert(num)
            else:
                self.small_half.insert(num)
        else:
            if num < self.small_half.max():
                self.big_half.insert(self.small_half.extract())
                self.small_half.insert(num)
            else:
                self.big_half.insert(num)

    def findMedian(self) -> float:
        if len(self.small_half) != len(self.big_half):
            return self.big_half.min()
        if len(self.big_half) == 0:
            return 0
        return (self.big_half.min() + self.small_half.max())/2


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
# @lc code=end

#
# @lc app=leetcode id=295 lang=python3
#
# [295] Find Median from Data Stream
#
from heapq import heappush, heappushpop

# @lc code=start


class MedianFinder:

    def __init__(self):
        self.min_heap = Heap()
        self.max_heap = Heap(False)

    def addNum(self, num: int) -> None:
        if not self.max_heap:
            self.max_heap.push(num)
            return
        if num >= self.max_heap[0]:
            if len(self.max_heap) > len(self.min_heap):
                self.min_heap.push(num)
            else:
                self.max_heap.push(self.min_heap.pushpop(num))
        else:
            if len(self.max_heap) > len(self.min_heap):
                self.min_heap.push(self.max_heap.pushpop(num))
            else:
                self.max_heap.push(num)

    def findMedian(self) -> float:
        if len(self.max_heap) > len(self.min_heap):
            return self.max_heap[0]
        else:
            return (self.min_heap[0] + self.max_heap[0]) / 2


class Heap:
    def __init__(self, min=True):
        self.min = min
        self.container = []

    def push(self, num):
        if self.min:
            heappush(self.container, num)
        else:
            heappush(self.container, -num)

    def pushpop(self, num):
        if self.min:
            return heappushpop(self.container, num)
        else:
            return -heappushpop(self.container, -num)

    def __len__(self):
        return len(self.container)

    def __getitem__(self, i):
        if self.min:
            return self.container[i]
        else:
            return -self.container[i]

    def __nonzero__(self):
        return bool(self.container)

    def __repr__(self) -> str:
        if self.min:
            return repr(self.container)
        else:
            return repr([-e for e in self.container])

# @lc code=end


def test_default():
    finder = MedianFinder()
    finder.addNum(2)
    finder.addNum(1)
    assert finder.findMedian() == 1.5
    finder.addNum(3)
    assert finder.findMedian() == 2.0


def test_corner_cases():
    finder = MedianFinder()
    finder.addNum(5)
    assert finder.findMedian() == 5

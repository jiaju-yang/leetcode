#
# @lc app=leetcode id=295 lang=python3
#
# [295] Find Median from Data Stream
#
from heapq import heappop, heappush, heappushpop

# @lc code=start


class MedianFinder:

    def __init__(self):
        self.large = []
        self.small = []

    def addNum(self, num: int) -> None:
        if len(self.large) == len(self.small):
            heappush(self.small, -heappushpop(self.large, num))
        else:
            heappush(self.large, -heappushpop(self.small, -num))

    def findMedian(self) -> float:
        if len(self.small) > len(self.large):
            return -self.small[0]
        else:
            return (self.large[0] - self.small[0]) / 2


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

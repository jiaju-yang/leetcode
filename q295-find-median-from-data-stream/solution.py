#
# @lc app=leetcode id=295 lang=python3
#
# [295] Find Median from Data Stream
#

# @lc code=start
from heapq import heapify, heappush, heappop


class MedianFinder:

    def __init__(self):
        self.large = []
        self.small = []

    def addNum(self, num: int) -> None:
        heappush(self.large, num)
        heappush(self.small, -heappop(self.large))
        if len(self.small) > len(self.large):
            heappush(self.large, -heappop(self.small))

    def findMedian(self) -> float:
        if len(self.large) == 0:
            return 0
        elif len(self.large) > len(self.small):
            return self.large[0]
        else:
            return (self.large[0] - self.small[0])/2


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
# @lc code=end

#
# @lc app=leetcode id=973 lang=python3
#
# [973] K Closest Points to Origin
#

# @lc code=start
from typing import List
from heapq import heapify, heappush, heappushpop, heappop


class HeapSolution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distances = [(-((point[0]**2) + (point[1]**2)), point[0], point[1])
                     for point in points]
        heap = []
        for i in range(k):
            heappush(heap, distances[i])
        for i in range(k, len(distances)):
            heappushpop(heap, distances[i])
        return [[distance[1], distance[2]] for distance in heap]


class AnotherHeapSolution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distances = [((point[0]**2) + (point[1]**2), point[0], point[1])
                     for point in points]
        heapify(distances)
        result = []
        for _ in range(k):
            distance = heappop(distances)
            result.append([distance[1], distance[2]])
        return result


Solution = AnotherHeapSolution
# @lc code=end

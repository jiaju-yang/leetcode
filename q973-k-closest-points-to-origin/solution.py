#
# @lc app=leetcode id=973 lang=python3
#
# [973] K Closest Points to Origin
#

# @lc code=start
from typing import List
from random import choice
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


class DivideAndConquerSolution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distances = [((point[0]**2) + (point[1]**2), point[0], point[1])
                     for point in points]
        self._find(distances, 0, len(distances) - 1, k)
        return [[distances[i][1], distances[i][2]] for i in range(k)]

    def _find(self, distances, p, r, k):
        pivot_index = self._partition(distances, p, r)
        if pivot_index == k - 1:
            return pivot_index
        elif pivot_index < k - 1:
            return self._find(distances, pivot_index + 1, r, k)
        else:
            return self._find(distances, p, pivot_index - 1, k)

    def _partition(self, distances, p, r):
        pivot_index = choice(range(r-p+1)) + p
        distances[pivot_index], distances[r] = distances[r], distances[pivot_index]
        i = p
        for j in range(p, r):
            if distances[j][0] < distances[r][0]:
                distances[i], distances[j] = distances[j], distances[i]
                i += 1
        distances[i], distances[r] = distances[r], distances[i]
        return i


Solution = DivideAndConquerSolution
# @lc code=end

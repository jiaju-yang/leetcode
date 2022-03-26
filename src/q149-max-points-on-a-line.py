#
# @lc app=leetcode id=149 lang=python3
#
# [149] Max Points on a Line
#
from typing import List
from collections import defaultdict


# @lc code=start
class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        if len(points) == 1:
            return 1
        lines = defaultdict(set)
        for i in range(len(points) - 1):
            for j in range(i + 1, len(points)):
                x1, y1 = points[i]
                x2, y2 = points[j]
                if x1 == x2:
                    k = float('inf')
                    m = x1
                elif y1 == y2:
                    k = 0
                    m = y1
                else:
                    a, b = y1-y2, x1-x2
                    while True:
                        d = self.gcd(a, b)
                        if d == 1 or d == -1:
                            break
                        a, b = a // d, b // d
                    k = (a, b)
                    a = a * x1
                    while True:
                        d = self.gcd(a, b)
                        if d == 1 or d == -1:
                            break
                        a, b = a // d, b // d
                    m = (y1 * b - a, b)
                lines[(k, m)].add(i)
                lines[(k, m)].add(j)
        return max(len(s) for s in lines.values())

    def gcd(self, a, b):
        if a < 0 and b < 0:
            return self.gcd(-a, -b)
        if a < 0:
            return -self.gcd(-a, b)
        if b < 0:
            return -self.gcd(a, -b)
        if b > a:
            return self.gcd(b, a)
        if b == 0:
            return a
        return self.gcd(b, a % b)


# @lc code=end
solve = Solution().maxPoints


def test_default():
    assert solve([[1, 1], [2, 2], [3, 3]]) == 3
    assert solve([[1, 1], [3, 2], [5, 3], [4, 1], [2, 3], [1, 4]]) == 4


def test_corner_cases():
    assert solve([[1, 1]]) == 1
    assert solve([[0, 0], [1, 1]]) == 2
    assert solve([[-1, -1], [1, 1]]) == 2
    assert solve([[1, 2], [1, 1]]) == 2
    assert solve([[2, 1], [1, 1]]) == 2
    assert solve([[-1, -1], [1, 1], [-1, 1], [1, -1]]) == 2

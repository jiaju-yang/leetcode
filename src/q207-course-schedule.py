#
# @lc app=leetcode id=207 lang=python3
#
# [207] Course Schedule
#
from typing import List
# @lc code=start


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        states = [0] * numCourses
        adjs = [[] for _ in range(numCourses)]
        for neighbor, node in prerequisites:
            adjs[node].append(neighbor)

        def dfs(node):
            states[node] = 1
            for adj in adjs[node]:
                if states[adj] == 1:
                    return True
                if states[adj] == 0:
                    cyclic = dfs(adj)
                    if cyclic:
                        return True
            states[node] = 2
            return False

        for node in range(numCourses):
            if states[node] == 0:
                cyclic = dfs(node)
                if cyclic:
                    return False
        return True


# @lc code=end


solve = Solution().canFinish


def test_default():
    assert solve(3, [[1, 0], [2, 1]])
    assert not solve(3, [[0, 1], [1, 2], [2, 0]])


def test_corners():
    assert solve(1, [])
    assert solve(2, [[0, 1]])
    assert not solve(2, [[1, 0], [0, 1]])

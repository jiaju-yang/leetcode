#
# @lc app=leetcode id=210 lang=python3
#
# [210] Course Schedule II
#

# @lc code=start
from typing import List


class Node:
    def __init__(self, name, color='white', adjs=None):
        if not adjs:
            adjs = []
        self.name = name
        self.color = color
        self.adjs = adjs


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        def dfs_visit(course):
            course.color = 'gray'
            for adj_name in course.adjs:
                adj = courses[adj_name]
                if adj.color == 'white':
                    if not dfs_visit(adj):
                        return False
                elif adj.color == 'gray':
                    return False
            course.color = 'black'
            result.append(course.name)
            return True

        courses = {i: Node(i) for i in range(numCourses)}
        for dependency in prerequisites:
            courses[dependency[0]].adjs.append(dependency[1])
        result = []
        for course in courses.values():
            if course.color == 'white':
                if not dfs_visit(course):
                    return []
        return result
# @lc code=end

#
# @lc app=leetcode id=210 lang=python3
#
# [210] Course Schedule II
#

# @lc code=start
from typing import List
from collections import deque


class Node:
    def __init__(self, name, color='white', adjs=None, indegree=0):
        if not adjs:
            adjs = []
        self.name = name
        self.color = color
        self.adjs = adjs
        self.indegree = indegree


class DFSSolution:
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


class BFSSolution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        courses = {i: Node(i) for i in range(numCourses)}
        for dependency in prerequisites:
            courses[dependency[0]].adjs.append(dependency[1])
            courses[dependency[1]].indegree += 1
        q = deque(course for course in courses.values() if not course.indegree)
        result = []
        while q:
            course = q.pop()
            for adj_name in course.adjs:
                adj_course = courses[adj_name]
                adj_course.indegree -= 1
                if not adj_course.indegree:
                    q.appendleft(adj_course)
            result.append(course.name)
        if len(result) != numCourses:
            return []
        return result[::-1]


Solution = BFSSolution
# @lc code=end

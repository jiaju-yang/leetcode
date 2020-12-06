#
# @lc app=leetcode id=207 lang=python3
#
# [207] Course Schedule
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
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        def dfs_visit(course):
            course.color = 'gray'
            for adj_course_name in course.adjs:
                adj_course = courses[adj_course_name]
                if adj_course.color == 'white':
                    result = dfs_visit(adj_course)
                    if not result:
                        return False
                elif adj_course.color == 'gray':
                    return False
            course.color = 'black'
            return True

        courses = {}
        for edge in prerequisites:
            try:
                courses[edge[0]].adjs.append(edge[1])
            except KeyError:
                courses[edge[0]] = Node(edge[0], adjs=[edge[1]])
            if edge[1] not in courses:
                courses[edge[1]] = Node(edge[1])
        for course in courses.values():
            if course.color == 'white':
                result = dfs_visit(course)
                if not result:
                    return False
        return True
# @lc code=end

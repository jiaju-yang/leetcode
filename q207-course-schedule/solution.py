#
# @lc app=leetcode id=207 lang=python3
#
# [207] Course Schedule
#

# @lc code=start
from typing import List
from collections import defaultdict


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        def dfs_visit(course):
            nonlocal time
            time += 1
            prop = courses[course]
            prop['d'] = time
            prop['color'] = 'gray'
            for adj_course in prop['adjs']:
                if courses[adj_course]['color'] == 'white':
                    result = dfs_visit(adj_course)
                    if not result:
                        return False
                elif courses[adj_course]['color'] == 'gray':
                    return False
            prop['color'] = 'black'
            time += 1
            prop['f'] = time
            return True


        courses = defaultdict(lambda: {
            'color': 'white',
            'pi': None,
            'd': None,
            'f': None,
            'adjs': []
        })
        for edge in prerequisites:
            courses[edge[0]]['adjs'].append(edge[1])
            courses[edge[1]]
        time = 0
        for course, prop in courses.items():
            if prop['color'] == 'white':
                result = dfs_visit(course)
                if not result:
                    return False
        return True
# @lc code=end

#
# @lc app=leetcode id=349 lang=python3
#
# [349] Intersection of Two Arrays
#

# @lc code=start
from typing import List


class BuiltinSolution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        return list(set(nums1).intersection(set(nums2)))


class TwoPointersSolution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()
        nums2.sort()
        p1, p2 = 0, 0
        result = []
        while p1 < len(nums1) and p2 < len(nums2):
            if nums1[p1] == nums2[p2]:
                result.append(nums1[p1])
                p1 += 1
                p2 += 1
                while p1 < len(nums1) and nums1[p1] == nums1[p1-1]:
                    p1 += 1
                while p2 < len(nums2) and nums2[p2] == nums2[p2-1]:
                    p2 += 1
            elif nums1[p1] < nums2[p2]:
                p1 += 1
                while p1 < len(nums1) and nums1[p1] == nums1[p1-1]:
                    p1 += 1
            else:
                p2 += 1
                while p2 < len(nums2) and nums2[p2] == nums2[p2-1]:
                    p2 += 1
        return result


Solution = TwoPointersSolution
# @lc code=end

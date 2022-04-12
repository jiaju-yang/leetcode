#
# @lc app=leetcode id=88 lang=python3
#
# [88] Merge Sorted Array
#
from typing import List

# @lc code=start


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if n == 0:
            return
        if m == 0:
            nums1[:] = nums2[:]
            return
        insert_index = len(nums1) - 1
        i, j = m - 1, n - 1
        while insert_index >= 0:
            if i < 0:
                nums1[insert_index] = nums2[j]
                insert_index -= 1
                j -= 1
            elif j < 0:
                nums1[insert_index] = nums1[i]
                insert_index -= 1
                i -= 1
            elif nums1[i] < nums2[j]:
                nums1[insert_index] = nums2[j]
                insert_index -= 1
                j -= 1
            else:
                nums1[insert_index] = nums1[i]
                insert_index -= 1
                i -= 1


# @lc code=end
solve = Solution().merge


def test_default():
    nums1 = [1, 2, 3, 0, 0, 0]
    solve(nums1, 3, [2, 5, 6], 3)
    assert nums1 == [1, 2, 2, 3, 5, 6]


def test_corner_cases():
    nums1 = [1]
    solve(nums1, 1, [], 0)
    assert nums1 == [1]

    nums1 = [0]
    solve(nums1, 0, [1], 1)
    assert nums1 == [1]

    nums1 = [1, 0]
    solve(nums1, 1, [2], 1)
    assert nums1 == [1, 2]

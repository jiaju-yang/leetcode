#
# @lc app=leetcode id=744 lang=python3
#
# [744] Find Smallest Letter Greater Than Target
#

# @lc code=start
from typing import List


class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        left, right = 0, len(letters) - 1
        target_ord = ord(target)
        while left <= right:
            middle = (left + right) >> 1
            if letters[middle] == target:
                break
            elif ord(letters[middle]) < target_ord:
                left = middle + 1
            else:
                right = middle - 1
        while middle < len(letters) - 1 and letters[middle] == letters[middle + 1]:
            middle += 1
        return letters[middle] if ord(letters[middle]) > target_ord else letters[(middle + 1) % len(letters)]

# @lc code=end

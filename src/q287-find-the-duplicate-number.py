#
# @lc app=leetcode id=287 lang=python3
#
# [287] Find the Duplicate Number
#
from typing import List

# @lc code=start


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow, fast = 0, 0
        while True:
            slow, fast = nums[slow], nums[nums[fast]]
            if slow == fast:
                break
        slow = previous = 0
        while slow != fast:
            previous, slow, fast = slow, nums[slow], nums[fast]
        return nums[previous]


# @lc code=end
solve = Solution().findDuplicate


def test_default():
    assert solve([1, 3, 4, 2, 2]) == 2
    assert solve([3, 1, 3, 4, 2]) == 3
    assert solve([2, 2, 2, 2, 2]) == 2
    assert solve([1, 3, 2, 1, 4]) == 1


def test_corner_cases():
    assert solve([1, 1]) == 1
    assert solve([1, 2, 2]) == 2

#
# @lc app=leetcode id=141 lang=python3
#
# [141] Linked List Cycle
#
from typing import Optional
from .linkedlist_tools import *

# @lc code=start


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow, fast = head, head
        try:
            while True:
                slow = slow.next
                fast = fast.next.next
                if slow is fast:
                    return True
        except AttributeError:
            return False


# @lc code=end
solve = Solution().hasCycle


def test_default():
    assert solve(construct_linkedlist([3, 2, 0, -4], 1))


def test_corner_cases():
    assert solve(construct_linkedlist([1, 2], 0))
    assert not solve(construct_linkedlist([1]))

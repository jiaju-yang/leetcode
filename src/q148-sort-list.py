#
# @lc app=leetcode id=148 lang=python3
#
# [148] Sort List
#
from typing import Optional
from .linkedlist_tools import *
# @lc code=start


class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        l = []
        while head:
            l.append(head)
            head = head.next
        l.sort(key=lambda n: n.val)
        head = cur = ListNode()
        for node in l:
            cur.next = node
            cur = node
        cur.next = None
        return head.next


# @lc code=end
solve = Solution().sortList


def test_default():
    assert solve(construct_linkedlist(
        [4, 2, 1, 3])) == construct_linkedlist([1, 2, 3, 4])
    assert solve(construct_linkedlist(
        [-1, 5, 3, 4, 0])) == construct_linkedlist([-1, 0, 3, 4, 5])


def test_corner_cases():
    assert solve(None) is None
    assert solve(construct_linkedlist([1])) == construct_linkedlist([1])
    assert solve(construct_linkedlist([2, 1])) == construct_linkedlist([1, 2])

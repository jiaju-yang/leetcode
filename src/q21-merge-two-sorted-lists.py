#
# @lc app=leetcode id=21 lang=python3
#
# [21] Merge Two Sorted Lists
#
from typing import Optional
from .linkedlist_tools import *
# @lc code=start


class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        curr = dummy
        while l1 and l2:
            if l1.val <= l2.val:
                curr.next = l1
                l1 = l1.next
            else:
                curr.next = l2
                l2 = l2.next
            curr = curr.next
        curr.next = l1 if l1 else l2
        return dummy.next

# @lc code=end


solve = Solution().mergeTwoLists


def test_default():
    assert solve(construct_LinkedList([1, 2, 4]), construct_LinkedList(
        [1, 3, 4])) == construct_LinkedList([1, 1, 2, 3, 4, 4])


def test_corner_cases():
    assert solve(construct_LinkedList([]), construct_LinkedList(
        [])) == construct_LinkedList([])
    assert solve(construct_LinkedList([]), construct_LinkedList([0])
                 ) == construct_LinkedList([0])
    assert solve(construct_LinkedList([1]), construct_LinkedList([0])
                 ) == construct_LinkedList([0, 1])

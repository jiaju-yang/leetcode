#
# @lc app=leetcode id=19 lang=python3
#
# [19] Remove Nth Node From End of List
#
from typing import Optional
from .linkedlist_tools import *

# @lc code=start


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        previous, end = dummy, head
        for _ in range(n):
            end = end.next
        while end:
            previous = previous.next
            end = end.next
        previous.next = previous.next.next
        return dummy.next


# @lc code=end
solve = Solution().removeNthFromEnd


def test_default():
    assert solve(construct_LinkedList(
        [1, 2, 3, 4, 5]), 2) == construct_LinkedList([1, 2, 3, 5])


def test_corner_cases():
    assert solve(construct_LinkedList([1]), 1) == construct_LinkedList([])
    assert solve(construct_LinkedList([1, 2]), 1) == construct_LinkedList([1])

#
# @lc app=leetcode id=143 lang=python3
#
# [143] Reorder List
#
from typing import Optional
from collections import deque
from .linkedlist_tools import *

# @lc code=start


class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        q = deque()
        while head:
            q.append(head)
            head = head.next
        previous = dummy = ListNode()
        while q:
            previous.next = q.popleft()
            previous.next.next = q.pop() if q else None
            previous = previous.next.next
        if previous:
            previous.next = None
        return dummy.next

# @lc code=end


solve = Solution().reorderList


def test_default():
    assert solve(construct_linkedlist(
        [1, 2, 3, 4])) == construct_linkedlist([1, 4, 2, 3])
    assert solve(construct_linkedlist(
        [1, 2, 3, 4, 5])) == construct_linkedlist([1, 5, 2, 4, 3])


def test_corner_cases():
    assert solve(construct_linkedlist([1])) == construct_linkedlist([1])
    assert solve(construct_linkedlist([1, 2])) == construct_linkedlist([1, 2])
    assert solve(construct_linkedlist(
        [1, 2, 3])) == construct_linkedlist([1, 3, 2])

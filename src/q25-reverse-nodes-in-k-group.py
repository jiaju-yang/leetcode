#
# @lc app=leetcode id=25 lang=python3
#
# [25] Reverse Nodes in k-Group
#
from typing import Optional
from .linkedlist_tools import *

# @lc code=start


class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        next_list, prev = head, None
        for _ in range(k):
            if not next_list:
                return head
            prev = next_list
            next_list = next_list.next
        prev.next = None
        new_head, new_tail = self.reverse(head)
        new_tail.next = self.reverseKGroup(next_list, k)
        return new_head

    def reverse(self, head):
        if not head:
            return None, None
        prev, cur, next = None, head, head.next
        while cur:
            next = cur.next
            cur.next = prev
            prev = cur
            cur = next
        return prev, head


# @lc code=end
solve = Solution().reverseKGroup


def test_default():
    assert solve(construct_linkedlist(
        [1, 2, 3, 4, 5]), 2) == construct_linkedlist([2, 1, 4, 3, 5])
    assert solve(construct_linkedlist(
        [1, 2, 3, 4, 5]), 3) == construct_linkedlist([3, 2, 1, 4, 5])


def test_corner_cases():
    assert solve(construct_linkedlist([1]), 1) == construct_linkedlist([1])
    assert solve(construct_linkedlist(
        [1, 2]), 1) == construct_linkedlist([1, 2])
    assert solve(construct_linkedlist(
        [1, 2]), 2) == construct_linkedlist([2, 1])

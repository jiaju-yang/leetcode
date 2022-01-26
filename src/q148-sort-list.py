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
        if not head or not head.next:
            return head
        prev_middle = self.get_prev_middle(head)
        middle = prev_middle.next
        prev_middle.next = None
        first = self.sortList(head)
        second = self.sortList(middle)
        return self.merge(first, second)

    def merge(self, n1, n2):
        head = cur = ListNode()
        while n1 and n2:
            if n1.val > n2.val:
                cur.next = n2
                n2 = n2.next
            else:
                cur.next = n1
                n1 = n1.next
            cur = cur.next
        cur.next = n2 if not n1 else n1
        return head.next

    def get_prev_middle(self, head):
        slow = fast = ListNode(None, head)
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow


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

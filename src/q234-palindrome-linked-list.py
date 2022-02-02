#
# @lc app=leetcode id=234 lang=python3
#
# [234] Palindrome Linked List
#
from typing import Optional
from .linkedlist_tools import *

# @lc code=start


class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        dummy = ListNode(next=head)
        slow = fast = dummy
        next = slow.next
        while fast and fast.next:
            fast = fast.next.next
            prev = slow
            slow = next
            next = slow.next
            slow.next = prev
        left, right = (slow, next) if fast else (prev, next)
        while right:
            if left.val != right.val:
                return False
            left, right = left.next, right.next
        return True


# @lc code=end
solve = Solution().isPalindrome


def test_default():
    assert solve(construct_linkedlist([1, 2, 2, 1]))
    assert not solve(construct_linkedlist([1, 2, 3, 1]))
    assert solve(construct_linkedlist([1, 2, 3, 2, 1]))


def test_corner_cases():
    assert not solve(construct_linkedlist([1, 2]))
    assert solve(construct_linkedlist([1]))

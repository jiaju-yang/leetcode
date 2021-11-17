#
# @lc app=leetcode id=206 lang=python3
#
# [206] Reverse Linked List
#
from typing import List, Optional
from .linkedlist_tools import *

# @lc code=start


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        previous, current = None, head
        while current:
            current.next, previous, current = previous, current, current.next
        return previous


# @lc code=end
solve = Solution().reverseList


def test_default():
    assert solve(construct_LinkedList(
        [1, 2, 3, 4, 5])) == construct_LinkedList([5, 4, 3, 2, 1])


def test_corner_cases():
    assert solve(None) == None
    assert solve(construct_LinkedList([1])) == construct_LinkedList([1])
    assert solve(construct_LinkedList([1, 2])) == construct_LinkedList([2, 1])

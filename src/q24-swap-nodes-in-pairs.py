#
# @lc app=leetcode id=24 lang=python3
#
# [24] Swap Nodes in Pairs
#
from typing import Optional
from .linkedlist_tools import *

# @lc code=start


class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        if not head.next:
            return head
        dummy = ListNode(next=head.next)
        head.next = self.swapPairs(head.next.next)
        dummy.next.next = head
        return dummy.next


# @lc code=end
solve = Solution().swapPairs


def test_default():
    assert solve(construct_linkedlist(
        [1, 2, 3, 4])) == construct_linkedlist([2, 1, 4, 3])


def test_corner_cases():
    assert solve(None) is None
    assert solve(construct_linkedlist([1])) == construct_linkedlist([1])
    assert solve(construct_linkedlist([1, 2])) == construct_linkedlist([2, 1])
    assert solve(construct_linkedlist(
        [1, 2, 3])) == construct_linkedlist([2, 1, 3])

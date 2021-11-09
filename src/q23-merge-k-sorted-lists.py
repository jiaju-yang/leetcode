#
# @lc app=leetcode id=23 lang=python3
#
# [23] Merge k Sorted Lists
#
from typing import List, Optional
from heapq import heapify, heappop, heappush
from .linkedlist_tools import *

# @lc code=start


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = [(lists[i].val, i, lists[i])
                for i in range(len(lists)) if lists[i]]
        heapify(heap)
        dummy = current = ListNode(None)
        while heap:
            val, i, node = heappop(heap)
            if node.next:
                heappush(heap, (node.next.val, i, node.next))
            current.next = ListNode(val)
            current = current.next
        return dummy.next


# @lc code=end


solve = Solution().mergeKLists


def test_default():
    assert solve(construct_multi_list([[1, 4, 5], [1, 3, 4], [
                 2, 6]])) == construct_LinkedList([1, 1, 2, 3, 4, 4, 5, 6])


def test_corners():
    assert solve([]) == None
    assert solve([None]) == None
    assert solve([ListNode(1)]) == ListNode(1)

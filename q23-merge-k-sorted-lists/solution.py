#
# @lc app=leetcode id=23 lang=python3
#
# [23] Merge k Sorted Lists
#

# @lc code=start
from typing import List
from heapq import heapify, heappop, heappush
# Definition for singly-linked list.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __eq__(self, other):
        if not isinstance(other, ListNode):
            return False
        return self.val == other.val

    def __repr__(self):
        return 'Node({})'.format(self.val)


class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        heap = [(node.val, i) for i, node in enumerate(lists)
                if node is not None and node.val is not None]
        heapify(heap)
        head = curr = None
        while heap:
            val, i = heappop(heap)
            node = lists[i]
            if not head:
                head = curr = ListNode(val)
            else:
                curr.next = ListNode(val)
                curr = curr.next
            if node.next:
                heappush(heap, (node.next.val, i))
            lists[i] = lists[i].next
        return head

# @lc code=end

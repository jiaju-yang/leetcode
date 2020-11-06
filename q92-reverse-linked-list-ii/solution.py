#
# @lc app=leetcode id=92 lang=python3
#
# [92] Reverse Linked List II
#

# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __eq__(self, other):
        if not isinstance(other, ListNode):
            return False
        return self.val == other.val and self.next == other.next

    def __hash__(self):
        return hash(self.val)

    def __repr__(self):
        values = [self.val]
        current = self
        while current.next:
            current = current.next
            values.append(current.val)
        return 'LinkedList({})'.format(str(values))


class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        if m == n:
            return head
        current, first_half_tail = head, None
        for _ in range(m-1):
            first_half_tail = current
            current = current.next
        reversed_head, reversed_tail, next_half = self._revserse_part(current, n-m)
        if first_half_tail:
            first_half_tail.next = reversed_head
        else:
            head = reversed_head
        reversed_tail.next = next_half
        return head

    def _revserse_part(self, head, length):
        new_tail = current = head
        previous = None
        while length >= 0:
            next_node = current.next
            current.next = previous
            previous = current
            current = next_node
            length -= 1
        return (previous, new_tail, current)

# @lc code=end

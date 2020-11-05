#
# @lc app=leetcode id=206 lang=python3
#
# [206] Reverse Linked List
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
        return str(self.val)


class IterativeSolution:
    def reverseList(self, head: ListNode) -> ListNode:
        current, previous = head, None
        while current:
            next_node = current.next
            current.next = previous
            previous = current
            current = next_node
        return previous


Solution = IterativeSolution
# @lc code=end

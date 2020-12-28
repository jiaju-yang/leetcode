#
# @lc app=leetcode id=142 lang=python3
#
# [142] Linked List Cycle II
#

# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class SetSolution:
    def detectCycle(self, head: ListNode) -> ListNode:
        detected = set()
        cur = head
        while cur:
            if cur in detected:
                return cur
            detected.add(cur)
            cur = cur.next
        return None


class TwoPointersSolution:
    def detectCycle(self, head: ListNode) -> ListNode:
        slow, fast = head, head
        while True:
            try:
                slow = slow.next
                fast = fast.next.next
                if slow is fast:
                    break
            except AttributeError:
                return None
        first, second = head, fast
        while first is not second:
            first = first.next
            second = second.next
        return first


Solution = TwoPointersSolution
# @lc code=end

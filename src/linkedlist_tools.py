from typing import List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __eq__(self, other):
        if not isinstance(other, ListNode):
            return False
        return self.val == other.val and self.next == other.next

    def __repr__(self):
        return f'Node({self.val})'


def construct_LinkedList(values: List):
    previous = head = None
    for i in range(len(values)):
        current = ListNode(values[i])
        if not head:
            head = current
        if previous:
            previous.next = current
        previous = current
    return head


def construct_multi_list(values: List[List]) -> List[ListNode]:
    result = []
    for value in values:
        result.append(construct_LinkedList(value))
    return result

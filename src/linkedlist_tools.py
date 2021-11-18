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


def construct_linkedlist(values: List, pos=None):
    """
    Construct a linked list from list

    :param pos: if there is a cycle in the linked list, pass the index of the node that the last node should point to.
    """
    previous = head = pos_node = None
    for i in range(len(values)):
        current = ListNode(values[i])
        if not head:
            head = current
        if previous:
            previous.next = current
        previous = current
        if i == pos:
            pos_node = current
        if i == len(values) - 1:
            current.next = pos_node
    return head


def construct_multi_list(values: List[List]) -> List[ListNode]:
    result = []
    for value in values:
        result.append(construct_linkedlist(value))
    return result

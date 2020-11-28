from solution import Solution, ListNode
from typing import List

solve = Solution().mergeKLists


def construct_LinkedList(values: List, pos: int):
    previous = head = pos_node = None
    for i in range(len(values)):
        current = ListNode(values[i])
        if previous:
            previous.next = current
        previous = current
        if i == 0:
            head = current
        if i == pos:
            pos_node = current
        if i == len(values) - 1:
            current.next = pos_node
    return head


def test_default():
    assert solve([construct_LinkedList([1, 4, 5], None), construct_LinkedList(
        [1, 3, 4], None), construct_LinkedList([2, 6], None)]) == construct_LinkedList([1, 1, 2, 3, 4, 4, 5, 6], None)


def test_corner_cases():
    assert solve([]) == None
    assert solve([ListNode(None, None)]) == None

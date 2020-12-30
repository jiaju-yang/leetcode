from solution import Solution, ListNode
from typing import List

solve = Solution().middleNode


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


def test_existing_cycle():
    assert solve(construct_LinkedList([1, 2, 3, 4, 5], -1)).val == 3
    assert solve(construct_LinkedList([1, 2, 3, 4, 5, 6], -1)).val == 4


def test_corner_cases():
    assert solve(construct_LinkedList([1], -1)).val == 1
    assert solve(construct_LinkedList([1, 2], -1)).val == 2

from typing import List
from solution import Solution, ListNode

solve = Solution().reverseBetween


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
    assert solve(construct_LinkedList(
        [1, 2, 3, 4, 5], None), 2, 4) == construct_LinkedList([1, 4, 3, 2, 5], None)


def test_reverse_from_head():
    assert solve(construct_LinkedList(
        [1, 2, 3, 4, 5], None), 1, 2) == construct_LinkedList([2, 1, 3, 4, 5], None)
    assert solve(construct_LinkedList(
        [1, 2], None), 1, 2) == construct_LinkedList([2, 1], None)


def test_corner_cases():
    assert solve(construct_LinkedList(
        [1], None), 1, 1) == construct_LinkedList([1], None)
    assert solve(construct_LinkedList(
        [1, 2, 3], None), 2, 3) == construct_LinkedList([1, 3, 2], None)
    assert solve(construct_LinkedList(
        [], None), 0, 0) == construct_LinkedList([], None)

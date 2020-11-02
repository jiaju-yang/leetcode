from solution import Solution, ListNode
from typing import List

solve = Solution().hasCycle


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
    assert solve(construct_LinkedList([3, 2, 0, -4], 1)) is True
    assert solve(construct_LinkedList([1, 2], 0)) is True


def test_not_existing_cycle():
    assert solve(construct_LinkedList([1], -1)) is False
    assert solve(construct_LinkedList([1, 3, 0, 4], -1)) is False


def test_corner_cases():
    assert solve(construct_LinkedList([1], 0)) is True
    assert solve(construct_LinkedList([], -1)) is False

from typing import List
from solution import Solution, ListNode

solve = Solution().reverseList


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
        [1, 2, 3, 4, 5], None)) == construct_LinkedList([5, 4, 3, 2, 1], None)


def test_corner_cases():
    assert solve(construct_LinkedList(
        [1], None)) == construct_LinkedList([1], None)
    assert solve(construct_LinkedList(
        [1, 2], None)) == construct_LinkedList([2, 1], None)
    assert solve(construct_LinkedList([], None)
                 ) == construct_LinkedList([], None)

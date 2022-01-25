#
# @lc app=leetcode id=146 lang=python3
#
# [146] LRU Cache
#
from collections import namedtuple

# @lc code=start

Element = namedtuple('Element', 'key value')


class Node:
    def __init__(self, element, previous=None, next=None) -> None:
        self.element = element
        self.previous = previous
        self.next = previous


class DoublyLinkedList:
    def __init__(self) -> None:
        self.head = self.tail = Node(None)
        self.head.next = self.tail
        self.tail.previous = self.head
        self.size = 0

    def pop(self):
        if self.size == 0:
            return
        ret = self.tail.previous
        last_second = ret.previous
        self.tail.previous = last_second
        last_second.next = self.tail
        self.size -= 1
        return ret.element

    def appendleft(self, element):
        new = Node(element)
        self._insert_node_to_head(new)
        self.size += 1

    def move_to_head(self, node):
        previous = node.previous
        next = node.next
        previous.next = next
        next.previous = previous
        self._insert_node_to_head(node)

    def first(self):
        return self.head.next

    def _insert_node_to_head(self, node):
        first = self.head.next
        node.next = first
        node.previous = self.head
        first.previous = node
        self.head.next = node


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.size = 0
        self.queue = DoublyLinkedList()
        self.map = {}

    def get(self, key: int) -> int:
        if key not in self.map:
            return -1
        node = self.map[key]
        self.queue.move_to_head(node)
        return node.element.value

    def put(self, key: int, value: int) -> None:
        if key in self.map:
            self.map[key].element = Element(key, value)
            self.queue.move_to_head(self.map[key])
        else:
            new = Element(key, value)
            self.queue.appendleft(new)
            self.map[key] = self.queue.first()
            self.size += 1
        if self.size > self.capacity:
            victim = self.queue.pop()
            del self.map[victim.key]
            self.size -= 1


# @lc code=end


def test_default():
    lru = LRUCache(2)
    lru.put(1, 1)
    lru.put(2, 2)
    assert lru.get(1) == 1
    lru.put(3, 3)
    assert lru.get(2) == -1
    lru.put(4, 4)
    assert lru.get(1) == -1
    assert lru.get(3) == 3
    assert lru.get(4) == 4

    lru = LRUCache(2)
    lru.put(2, 1)
    lru.put(2, 2)
    assert lru.get(2) == 2
    lru.put(1, 1)
    lru.put(4, 1)
    assert lru.get(2) == -1

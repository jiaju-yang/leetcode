#
# @lc app=leetcode id=138 lang=python3
#
# [138] Copy List with Random Pointer
#
from itertools import count
from typing import Optional
# Definition for a Node.


class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

# @lc code=start


class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        prev = ret = Node(0)
        mapping = {}
        while head:
            if head not in mapping:
                mapping[head] = Node(head.val)
            prev.next = mapping[head]
            prev = prev.next
            if head.random is not None and head.random not in mapping:
                mapping[head.random] = Node(head.random.val)
            if head.random is not None:
                mapping[head].random = mapping[head.random]
            head = head.next
        return ret.next
# @lc code=end

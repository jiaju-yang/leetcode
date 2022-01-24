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
        vals = []
        addr_to_index = {}
        cur = head
        count = 0
        while cur:
            vals.append(Node(cur.val))
            addr_to_index[cur] = count
            count += 1
            cur = cur.next

        randoms = []
        cur = head
        while cur:
            if cur.random:
                randoms.append(addr_to_index[cur.random])
            else:
                randoms.append(None)
            cur = cur.next

        ret = Node(1)
        cur = ret
        for i in range(len(vals)):
            cur.next = vals[i]
            if randoms[i] is not None:
                cur.next.random = vals[randoms[i]]
            cur = cur.next
        return ret.next
# @lc code=end

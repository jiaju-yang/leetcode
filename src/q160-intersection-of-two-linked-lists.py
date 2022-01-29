#
# @lc app=leetcode id=160 lang=python3
#
# [160] Intersection of Two Linked Lists
#
from typing import Optional
from .linkedlist_tools import *

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        a, b = headA, headB
        while a is not b:
            a = a.next if a else headB
            b = b.next if b else headA
        return a if a else None

# @lc code=end

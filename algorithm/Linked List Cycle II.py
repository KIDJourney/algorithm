#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: kidjourney
# @Date:   2015-04-29 21:19:04
# @Last Modified by:   kidjourney
# @Last Modified time: 2015-04-29 21:22:25
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @return a list node
    def detectCycle(self, head):
        if head is None :
            return None 
        slow = head
        fast = head
        while fast.next and fast.next.next :
            slow = slow.next
            fast = fast.next.next
            if slow == fast :
                break
        else :
            return None
        new = head
        while new != slow :
            new = new.next
            slow = slow.next
        
        return new
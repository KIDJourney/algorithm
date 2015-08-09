#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: kidjourney
# @Date:   2015-03-31 19:48:23
# @Last Modified by:   kidjourney
# @Last Modified time: 2015-03-31 20:38:31
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param two ListNodes
    # @return a ListNode
    def mergeTwoLists(self, l1, l2):
        head = ListNode(0)
        temp = head 
        while (l1 and l2) :
            if l1.val < l2.val :
                temp.next = l1 
                l1 = l1.next
            else :
                temp.next = l2 
                l2 = l2.next
            temp = temp.next
        while (l1) :
            temp.next = l1 
            l1 = l1.next
            temp = temp.next
        while (l2) :
            temp.next = l2
            l2 = l2.next 
            temp = temp.next
        return head.next
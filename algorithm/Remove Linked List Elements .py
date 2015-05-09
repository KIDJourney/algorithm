#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: kidjourney
# @Date:   2015-05-09 09:01:49
# @Last Modified by:   kidjourney
# @Last Modified time: 2015-05-09 09:22:08
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param {ListNode} head
    # @param {integer} val
    # @return {ListNode}
    def removeElements(self, head, val):
        if head is None :
            return None
        newhead = ListNode(10)
        newhead.next = head
        temphead = newhead
        while temphead and temphead.next :
            if temphead.next.val == val :
                temphead.next = temphead.next.next
            else :
                temphead = temphead.next
        return newhead.next
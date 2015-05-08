#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: kidjourney
# @Date:   2015-05-08 21:26:32
# @Last Modified by:   kidjourney
# @Last Modified time: 2015-05-08 22:54:15
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param {ListNode} head
    # @return {ListNode}
    def reverseList(self, head):
        first = head
        temp = None
        pre = None

        while first :        
            temp = first
            first = first.next
            temp.next = pre
            pre = temp
        return temp 
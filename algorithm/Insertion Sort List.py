#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: kidjourney
# @Date:   2015-05-21 00:12:08
# @Last Modified by:   kidjourney
# @Last Modified time: 2015-05-21 20:36:25
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param {ListNode} head
    # @return {ListNode}
    def insertionSortList(self, head):
        if not head :
            return None
        ansnode = ListNode(0)
        while head :
            posnode = ansnode 
            while posnode.next and posnode.next.val < head.val :
                posnode = posnode.next
            nextnode = posnode.next
            posnode.next = head
            head = head.next
            posnode.next.next = nextnode           
        return ansnode.next
#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Position: E:\Program\LeetCoder_Python\remove-nth-node-from-end-of-list.py
# @Author: KIDJourney
# @Email: kingdeadfish@qq.com
# @Date:   2015-03-15
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @return a ListNode
    def removeNthFromEnd(self, head, n):
        pos = head 
        for _ in range(n-1) :
            if pos.next is None :
                return 
            pos = pos.next
        if pos.next is None :
            head = head.next
            return head
        else :
            pos = pos.next
            goal = head
            while pos.next is not None :
                pos = pos.next 
                goal = goal.next
            goal.next = goal.next.next
            return head
#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Position: E:\Program\algorithm\populating-next-right-pointers-in-each-node.py
# @Author: KIDJourney
# @Email: kingdeadfish@qq.com
# @Date:   2016-03-05
# Definition for binary tree with next pointer.
# class TreeLinkNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None

class Solution(object):
    def connect(self, root):
        """
        :type root: TreeLinkNode
        :rtype: nothing
        """
        self.node_list = []
        self.dfs(root , 1)
        for item in self.node_list :
            for index , value in enumerate(item[:-1]):
                item[index].next = item[index+1]

    def dfs(self, node , level):
        if node is None : return None

        if (level > len(self.node_list)):
            self.node_list.append([])
        
        self.node_list[level-1].append(node)
        
        self.dfs(node.left , level + 1)
        self.dfs(node.right , level + 1)

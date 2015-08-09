#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: kidjourney
# @Date:   2015-03-28 21:17:36
# @Last Modified by:   kidjourney
# @Last Modified time: 2015-03-28 21:37:24
# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    # @param root, a tree node
    # @return a boolean
    def isSymmetric(self, root):
        if not root :
            return True

        dp = collections.deque([(root.left,root.right)])
        while dp :
            node1 , node2 = dp.popleft()
            if not node1 and not node2 :
                continue
            if not node1 or not node2 :
                return False
            if node1.val != node2.val :
                return False
            dp.append((node1.left,node2.right))
            dp.append((node1.right,node2.left))
        
        return True

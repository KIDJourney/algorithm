#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: KIDJourney
# @Date:   2015-03-23 22:53:38
# @Last Modified by:   kidjourney
# @Last Modified time: 2015-03-31 21:13:01
# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return a boolean
    def isBalanced(self, root):
        self.flag = 1
        self.clu(root)
        if self.flag :
            return True
        else :
            return False

    def clu(self,node) :
        if not node :
            return 1
        if abs(self.clu(node.left) - self.clu(node.right)) > 1 :
            self.flag = 0
        return max(self.clu(node.left) , self.clu(node.right)) + 1
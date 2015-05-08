#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: kidjourney
# @Date:   2015-04-22 20:45:24
# @Last Modified by:   kidjourney
# @Last Modified time: 2015-05-08 21:24:51
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {boolean}
    def isBalanced(self, root):
        if root == None :
            return True
        return abs(self.getheight(root.left) - self.getheight(root.right)) <=1 and self.isBalanced(root.left) and self.isBalanced(root.right)



    def getheight(self,node):
        if  node  is None:
            return 1
        return max(self.getheight(node.left),self.getheight(node.right)) + 1 
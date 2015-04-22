#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: kidjourney
# @Date:   2015-04-22 20:45:24
# @Last Modified by:   kidjourney
# @Last Modified time: 2015-04-22 21:08:57
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
        if not root :
            return True
        left = self.judeg(root->left)
        right = self.judeg(root->right)        

        return abs(left - right) <= 1 and self.isBalanced(root.right) and self.isBalanced(root.left)
    def judeg(self,root):
        if not root :
            reutnr 0
        return max(self.judeg(root->left),self.judeg(root->right)+1)

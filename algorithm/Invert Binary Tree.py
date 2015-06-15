#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: kidjourney
# @Date:   2015-06-15 23:53:26
# @Last Modified by:   kidjourney
# @Last Modified time: 2015-06-15 23:56:03
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {TreeNode}
    def invertTree(self, root):
        self.inver(root)
        return root

    def inver(self,root) :
        if not root :
            return 
        
        root.left , root.right = root.right , root.left

        self.inver(root.left)
        self.inver(root.right)

#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: kidjourney
# @Date:   2015-03-28 20:49:28
# @Last Modified by:   kidjourney
# @Last Modified time: 2015-03-28 21:15:49
# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return a list of lists of integers
    def levelOrderBottom(self, root):
        if root == None :
            return []
        self.ans = {}
        self.dfs(root,0)
        return self.ans.values()[::-1]

    def dfs(self,node,deepth) :
        if node.left != None :
            self.dfs(node.left,deepth+1)
        if node.right != None :
            self.dfs(node.right,deepth+1)
        self.ans.setdefault(deepth,[])
        self.ans[deepth].append(node.val)


#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Position: E:\Program\algorithm\kth-smallest-element-in-a-bst.py
# @Author: KIDJourney
# @Email: kingdeadfish@qq.com
# @Date:   2016-03-05
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        self.step = 1
        self.value = []

    def dfs(self, node):

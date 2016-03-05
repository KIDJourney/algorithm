#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Position: E:\Program\algorithm\convert-sorted-array-to-binary-search-tree.py
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
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        return self.build_tree(nums)
        
    def build_tree(self , numList):
        if len(numList) == 0 :
            return None
        mid = len(numList)//2
        root = TreeNode(numList[mid])

        root.left = self.build_tree(numList[:mid])
        root.right = self.build_tree(numList[mid+1:])

        return root
#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Position: E:\Program\algorithm\search-insert-position.py
# @Author: KIDJourney
# @Email: kingdeadfish@qq.com
# @Date:   2016-03-05
class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        e = len(nums)-1
        s = 0
        while s <= e :
            mid = (s + e) // 2
            if target > nums[mid] : 
                s = mid + 1
            else :
                e = mid - 1
        return s
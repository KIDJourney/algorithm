#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: kidjourney
# @Date:   2015-06-17 11:41:39
# @Last Modified by:   kidjourney
# @Last Modified time: 2015-06-17 11:43:00
class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def findMin(self, nums):
        Min = nums 
        for i in nums :
            if i < Min :
                Min = i
        return Min
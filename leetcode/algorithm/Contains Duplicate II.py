#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: kidjourney
# @Date:   2015-06-15 18:14:20
# @Last Modified by:   kidjourney
# @Last Modified time: 2015-06-15 23:47:12
class Solution:
    # @param {integer[]} nums
    # @param {integer} k
    # @return {boolean}
    def containsNearbyDuplicate(self, nums, k):
        if len(nums) == 0 :
            return False
        posdict = {}
        for i in range(len(nums)) :
            if posdict.get(nums[i]) is not None :
                if i - posdict[nums[i]] <= k :
                    return True
                posdict[nums[i]] = i
            else :
                posdict[nums[i]] = i
        return False
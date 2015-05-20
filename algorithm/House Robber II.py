#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: kidjourney
# @Date:   2015-05-20 23:51:58
# @Last Modified by:   kidjourney
# @Last Modified time: 2015-05-21 00:09:17
class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def rob(self, nums):
        if len(nums) == 0:
            return 0
        if len(nums) <= 2:
            return max(nums)
        dp1 = [0] + nums[:-1]
        dp2 = [0] + nums[1:]
        for i in range(len(dp1))[2:] :
            dp1[i] = max(dp1[i-2] + dp1[i] , dp1[i-1])
        for i in range(len(dp2))[2:] :
            dp2[i] = max(dp2[i-2] + dp2[i] , dp2[i-1])
        return max(dp1[-1],dp2[-1])
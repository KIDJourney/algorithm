#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: kidjourney
# @Date:   2015-03-31 18:47:24
# @Last Modified by:   kidjourney
# @Last Modified time: 2015-03-31 19:46:03
class Solution:
    # @param num, a list of integer
    # @return an integer
    def rob(self, num):
        num = [0] + num
        for i in range(len(num))[2:] :
            num[i] = max(num[i-2] + num[i] , num[i-1])
        return num[-1]

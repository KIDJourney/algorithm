#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: kidjourney
# @Date:   2015-06-17 11:06:13
# @Last Modified by:   kidjourney
# @Last Modified time: 2015-06-17 11:39:49
class Solution:
    # @param {integer} m
    # @param {integer} n
    # @return {integer}
    def rangeBitwiseAnd(self, m, n):
        if m==n or m == 0 :
            return m
        temp = 1
        while temp < m :
            temp = temp << 1
            if temp > m and temp <= n :
                return 0
        ans = m
        for i in xrange(m+1,n+1) :
            ans = ans & i
        return ans
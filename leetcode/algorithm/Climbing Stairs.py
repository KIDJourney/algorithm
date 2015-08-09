#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: kidjourney
# @Date:   2015-03-31 17:33:07
# @Last Modified by:   kidjourney
# @Last Modified time: 2015-03-31 21:32:57
class Solution:
    # @param n, an integer
    # @return an integer
    def climbStairs(self, n):
        a , b = 1 , 2 
        for i in range(n-1) :
            a , b = b , a + b
        return a
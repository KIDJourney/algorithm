#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: kidjourney
# @Date:   2015-05-08 21:16:24
# @Last Modified by:   kidjourney
# @Last Modified time: 2015-05-08 23:10:56
class Solution:
    # @param {integer} n
    # @return {integer}
    def numTrees(self, n):
        mydir = {i:1 for i in range(n+1)[1:]}
        for i in range(n+1)[2:] :
            for j in range(n)[2:] :
                if i*j > n :
                    break
                else 
                    mydir[i*j] = 0
        sum(mydir.values[])


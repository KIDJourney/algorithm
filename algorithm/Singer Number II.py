#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: kidjourney
# @Date:   2015-04-02 13:41:10
# @Last Modified by:   kidjourney
# @Last Modified time: 2015-04-02 16:08:32
class Solution:
    # @param A, a list of integer
    # @return an integer
    def singleNumber(self, A):
        numDir = {}
        for i in A :
            numDir.setdefault(i,0)
            numDir[i] += 1
        ans = [A for A in numDir.keys() if numDir[A]!=3]
        return ans[0]
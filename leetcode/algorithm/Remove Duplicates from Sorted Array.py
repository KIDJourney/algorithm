#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: kidjourney
# @Date:   2015-03-29 21:18:44
# @Last Modified by:   kidjourney
# @Last Modified time: 2015-03-29 21:47:34
class Solution:
    # @param a list of integers
    # @return an integer
    def removeDuplicates(self, A):
        if not A :
            return 0
        pos = 1
        for i in range(len(A))[1:] :
            if A[i] == A[i-1] :
                continue
            else :
                A[pos] = A[i]
                pos += 1
        return pos

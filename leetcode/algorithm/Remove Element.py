#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: kidjourney
# @Date:   2015-03-31 17:11:04
# @Last Modified by:   kidjourney
# @Last Modified time: 2015-03-31 17:12:44
class Solution:
    # @param    A       a list of integers
    # @param    elem    an integer, value need to be removed
    # @return an integer
    def removeElement(self, A, elem):
        pos = 0;
        for i in A :
            if i != elem :
                A[pos] = i
                pos += 1
        return pos 
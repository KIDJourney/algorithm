#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: kidjourney
# @Date:   2015-03-31 21:33:25
# @Last Modified by:   kidjourney
# @Last Modified time: 2015-03-31 21:49:52
class Solution:
    # @param a, a string
    # @param b, a string
    # @return a string
    def addBinary(self, a, b):
        anslist = []
        a = list(a).reverse()
        b = list(b).reverse()

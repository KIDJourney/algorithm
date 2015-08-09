#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: kidjourney
# @Date:   2015-04-22 10:42:31
# @Last Modified by:   kidjourney
# @Last Modified time: 2015-04-22 10:51:11
class Solution:
    # @param {integer} n
    # @return {boolean}
    def isHappy(self, n):
        history = [n]
        while True :
            temp = str(n)
            n = sum(map(lambda x : int(x)**2,temp))
            if n == 1:
                return True
            if n in history :
                return False
            else :
                history.append(n)
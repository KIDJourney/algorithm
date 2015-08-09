#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: kidjourney
# @Date:   2015-04-01 19:49:07
# @Last Modified by:   kidjourney
# @Last Modified time: 2015-04-01 19:54:13
class Solution:
    # @param digits, a list of integer digits
    # @return a list of integer digits
    def plusOne(self, digits):
        length = len(digits)
        up = 1
        for i in range(length)[::-1] :
            digits[i] = digits[i] + up
            up = digits[i] / 10
            digits[i] = digits[i] % 10
        while (up) :
            digits.insert(0,up)
            up /= 10
        return digits
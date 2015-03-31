#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: kidjourney
# @Date:   2015-03-30 21:40:01
# @Last Modified by:   kidjourney
# @Last Modified time: 2015-03-30 21:43:14
class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        binary = bin(n)[2:]
        binary = '0'*(32-len(binary)) + binary
        binary = binary.reverse()
        return int(binary,2)
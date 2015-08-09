#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: kidjourney
# @Date:   2015-03-30 21:40:01
# @Last Modified by:   kidjourney
# @Last Modified time: 2015-03-31 18:45:41
class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        binary = bin(n)[2:]
        binary = '0'*(32-len(binary)) + binary
        binary = list(binary)
        binary = binary[::-1]
        binary = ''.join(binary)
        return int(binary,2)
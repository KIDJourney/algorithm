#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Position: E:\Program\LeetCoder_Python\Number of 1 Bits.py
# @Author: KIDJourney
# @Email: kingdeadfish@qq.com
# @Date:   2015-03-14
class Solution:
    # @param n, an integer
    # @return an integer
    def hammingWeight(self, n):
        ans = 0
        while (n) :
            ans += n % 2
            n /= 2
        return ans 

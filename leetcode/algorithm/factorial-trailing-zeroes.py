#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Position: E:\Program\LeetCoder_Python\factorial-trailing-zeroes.py
# @Author: KIDJourney
# @Email: kingdeadfish@qq.com
# @Date:   2015-03-14
class Solution:
    # @return an integer
    def trailingZeroes(self, n):
        ans = 0
        while (n):
            ans += n / 5
            n /= 5
        return ans

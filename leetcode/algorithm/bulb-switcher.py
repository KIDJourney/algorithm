#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Position: E:\Program\algorithm\leetcode\algorithm\bulb-switcher.py
# @Author: KIDJourney
# @Email: kingdeadfish@qq.com
# @Date:   2016-01-21
class Solution(object):
    def bulbSwitch(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 1 :
            return n
        ans = 1
        step = 3
        while True :
            n -= step
            if n <= 0 :
                break
            ans += 1
            step += 2
        return ans 
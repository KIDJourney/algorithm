#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Position: E:\Program\algorithm\leetcode\algorithm\power_of_three.py
# @Author: KIDJourney
# @Email: kingdeadfish@qq.com
# @Date:   2016-01-21
class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        temp = 3**20
        return n > 0 and temp % n == 0
#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Position: E:\Program\algorithm\leetcode\algorithm\nim-game.py
# @Author: KIDJourney
# @Email: kingdeadfish@qq.com
# @Date:   2015-10-17
class Solution(object):
    def canWinNim(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n < 3 :
            return True
        if n % 4 == 0 :
            return False
        return True
#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Position: E:\Program\LeetCoder_Python\length-of-last-word.py
# @Author: KIDJourney
# @Email: kingdeadfish@qq.com
# @Date:   2015-03-15
class Solution:
    # @param s, a string
    # @return an integer
    def lengthOfLastWord(self, s):
        s = s.strip()
        s = s.split(' ')
        if len(s) > 0 :
            return len(s[-1])
        else :
            return 0
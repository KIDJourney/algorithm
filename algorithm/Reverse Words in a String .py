#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: kidjourney
# @Date:   2015-06-17 22:30:53
# @Last Modified by:   kidjourney
# @Last Modified time: 2015-06-17 22:35:01
class Solution:
    # @param s, a string
    # @return a string
    def reverseWords(self, s):
        s = s.strip().split()[::-1]
        s = " ".join(s)
        return s
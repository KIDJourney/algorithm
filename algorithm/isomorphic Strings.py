#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: kidjourney
# @Date:   2015-04-29 19:05:04
# @Last Modified by:   kidjourney
# @Last Modified time: 2015-04-29 19:53:20
class Solution:
    # @param {string} s
    # @param {string} t
    # @return {boolean}
    def isIsomorphic(self, s, t):
        if s is None and t is None :
            return True
        if s == t:
            return True
        mapdir = {}
        lenght = len(s)
        for i in range(lenght) :
            if s[i] in mapdir :
                if mapdir[s[i]] != t[i] :
                    return False
            else :
                if t[i] in t[0:i] :
                    return False
                mapdir[s[i]] = t[i]

        return True

# job = Solution()
# print job.isIsomorphic('ab','aa')
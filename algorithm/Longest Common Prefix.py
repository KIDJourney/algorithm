#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: kidjourney
# @Date:   2015-04-02 15:45:54
# @Last Modified by:   kidjourney
# @Last Modified time: 2015-04-02 15:48:17
class Solution:
    # @return a string
    def longestCommonPrefix(self, strs):
        if not strs :
            return ''
        ans = len(strs[0])
        for string in strs :
            ans = min(ans,len(string))
            while string[:ans] != strs[0][:ans] :
                ans -= 1
        if ans :
            return strs[0][:ans]
        else :
            return ''
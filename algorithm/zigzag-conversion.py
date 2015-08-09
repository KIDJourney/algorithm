#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Position: E:\Program\LeetCoder_Python\zigzag-conversion.py
# @Author: KIDJourney
# @Email: kingdeadfish@qq.com
# @Date:   2015-03-14
class Solution:
    # @return a string
    def convert(self, s, nRows) :
        strlen = len(s)
        pos = 0
        ans = [[] for _ in range(nRows)]
        while (pos<strlen) :
            for i in ans :
                if pos >= strlen :
                    break
                i.append(s[pos])
                pos += 1
            for i in ans[-2:0:-1] :
                if pos >= strlen :
                    break
                i.append(s[pos])
                pos += 1
        return ''.join(''.join(r) for r in ans)
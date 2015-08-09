#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: kidjourney
# @Date:   2015-04-22 11:33:39
# @Last Modified by:   kidjourney
# @Last Modified time: 2015-04-22 11:52:04
def getnext(string) : 
    m = len(string)
    next = [0 for i in range(m)]
    next[0] = -1
    k = -1
    j = 0
    while j < m -1 :
        if k == -1 or string[j] == string[k] :
            k += 1
            j += 1
            if string[j] != string[k] :
                next[j] = k
            else :
                next[j] = next[k]
        else :
            k = next[k]

    return next
print getnext("AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT")

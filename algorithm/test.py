#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: kidjourney
# @Date:   2015-05-08 22:40:08
# @Last Modified by:   kidjourney
# @Last Modified time: 2015-05-08 23:15:30
n = 3
mydir = {i:1 for i in range(n)[2:]}
for i in range(n+1)[2:] :
    for j in range(n)[2:] :
        if i*j > n :
            break
        else :
            mydir[i*j] = 0
print sum(mydir.values())

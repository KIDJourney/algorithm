#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: kidjourney
# @Date:   2015-06-15 23:35:16
# @Last Modified by:   kidjourney
# @Last Modified time: 2015-06-17 11:07:22
n = 7 
m = 5
ans = m
for i in range(m+1,n+1) :
    ans = ans & i
print( ans)
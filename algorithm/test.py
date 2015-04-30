#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: kidjourney
# @Date:   2015-04-29 19:48:35
# @Last Modified by:   kidjourney
# @Last Modified time: 2015-04-29 21:29:06
A = "^__^" 
B = "T.T"
for i in range(10) :
    C = A + B
    A , B = B , C
    print C

#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: kidjourney
# @Date:   2015-06-17 22:50:53
# @Last Modified by:   kidjourney
# @Last Modified time: 2015-06-19 00:20:28
def show(a,b) :
    print(a,b)

mystack = [1,2,3,4]
show(mystack.pop() , (mystack.pop()))
mystack = [1,2,3,4]
show(mystack.pop() , mystack.pop())

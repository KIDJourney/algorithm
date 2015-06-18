#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: kidjourney
# @Date:   2015-06-17 22:45:12
# @Last Modified by:   kidjourney
# @Last Modified time: 2015-06-19 00:35:27
class Solution:
    # @param {string[]} tokens
    # @return {integer}
    def evalRPN(self, tokens):
        stack = []
        symbolmap = {'+': lambda y,x : x+y ,
                     '-': lambda y,x : x-y ,
                     '*': lambda y,x : x*y ,
                     '/': lambda y,x : int(operator.truediv(x,y))}
        for i in tokens :
            if i in symbolmap :
                stack.append(symbolmap[i]((stack.pop()) , stack.pop()))
            else :
                stack.append(int(i))
        return stack[0]
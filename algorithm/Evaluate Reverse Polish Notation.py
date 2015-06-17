#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: kidjourney
# @Date:   2015-06-17 22:45:12
# @Last Modified by:   kidjourney
# @Last Modified time: 2015-06-17 23:02:29
class Solution:
    # @param {string[]} tokens
    # @return {integer}
    def evalRPN(self, tokens):
        stack = []
        symbol = ['+' , '-' , '*' , '/']
        for i in tokens :
            print(stack)
            if i in symbol :
                b = stack.pop()
                a = stack.pop()
                stack.append(int(eval("{0} {1} {2}".format(a,i,b))))
            else :
                stack.append(int(i))
        return int(stack[0])

job = Solution()
print(job.evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"]))
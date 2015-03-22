#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Position: E:\Program\LeetCoder_Python\algorithm\Pascal's Triangle II.py
# @Author: KIDJourney
# @Email: kingdeadfish@qq.com
# @Date:   2015-03-16
class Solution:
    # @return a list of integers
    def getRow(self, rowIndex):
        anslist = []
        for i in range(rowIndex+1) :
            anslist.append(self.select(rowIndex,i))
        return anslist
        
    def select(self,base,num):
        if num == 0 :
            return 1
        mom = 1
        kid = 1
        for i in range(base+1)[-num:]:
            kid *= i 
        for i in range(num+1)[1:] :
            mom *= i 
        return kid/mom
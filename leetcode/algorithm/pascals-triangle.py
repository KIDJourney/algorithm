#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Position: E:\Program\LeetCoder_Python\pascals-triangle.py
# @Author: KIDJourney
# @Email: kingdeadfish@qq.com
# @Date:   2015-03-14
class Solution:
    # @return a list of lists of integers
    def generate(self, numRows):
        if numRows == 0 :
            return []
        self.anslist = []
        for i in range(numRows) :
            templist = []
            for j in range(i+1) :
                templist.append(self.select(i,j))
            self.anslist.append(templist)
        return self.anslist
        
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
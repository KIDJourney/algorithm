#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Position: E:\Program\LeetCoder_Python\Count and Say.py
# @Author: KIDJourney
# @Email: kingdeadfish@qq.com
# @Date:   2015-02-01
class Solution:
    # @return a string
    def countAndSay(self, n):
        self.ans = "1"
        for i in range(n-1) :
            self.ans = self.doit()
        return self.ans

    def doit(self):
        temp = ""
        num = '0'
        nnum = 0
        lengh = len(self.ans)
        for i in range(lengh):
            if nnum == 0 :
                num = self.ans[0]
            if num != self.ans[i] :
                temp += str(nnum) + num
                num = self.ans[i]
                nnum = 1
            else :
                nnum += 1
            if i == lengh -1 :
                temp += str(nnum) + num
        return temp

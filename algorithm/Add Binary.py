#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: kidjourney
# @Date:   2015-03-31 21:33:25
# @Last Modified by:   kidjourney
# @Last Modified time: 2015-04-01 19:47:09
class Solution:
    # @param a, a string
    # @param b, a string
    # @return a string
    def addBinary(self, a, b):
        ans = ''
        pos = 0
        uplevel = 0
        a = a[::-1]
        b = b[::-1]
        lena , lenb = len(a) , len(b)
        while ( pos < lena and pos < lenb ) :
            tempsum = ord(a[pos]) + ord(b[pos]) +uplevel - ord('0')*2
            uplevel = tempsum / 2
            ans += str(tempsum%2)
            pos += 1

        while ( pos <lena ) :
            tempsum = ord(a[pos]) + uplevel - ord('0')
            uplevel = tempsum / 2
            ans += str(tempsum%2)
            pos += 1
        while (pos < lenb ) :
            tempsum = ord(b[pos]) + uplevel - ord('0')
            uplevel = tempsum / 2
            ans += str(tempsum%2)
            pos += 1
        if (uplevel==1) :
            ans += '1'
        return ans[::-1]

job = Solution()
print job.addBinary('1010','1011')
#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: kidjourney
# @Date:   2015-05-08 23:16:29
# @Last Modified by:   kidjourney
# @Last Modified time: 2015-05-08 23:36:29
class Solution:
    # @param {integer} n
    # @return {integer}
    def countPrimes(self, n):
        if n < 2 :
            return 0
        mydir = [0,0] + [1] * (n-2)
        i = 2
        while i < n :
            if mydir[i] :
                j = 2
                while i * j < n :
                    mydir[i*j] = 0
                    j += 1
            i += 1
        return sum(mydir)

job = Solution()
print (job.countPrimes(4))
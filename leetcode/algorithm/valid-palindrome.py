#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Position: E:\Program\LeetCoder_Python\valid-palindrome.py
# @Author: KIDJourney
# @Email: kingdeadfish@qq.com
# @Date:   2015-03-14
class Solution:
    # @param s, a string
    # @return a boolean
    def isPalindrome(self, s):
        string = s.upper()
        charlist = map(chr,range(ord('A'),ord('Z')+1))
        charlist+= map(str,range(10))
        string = ''.join([i for i in string if i in charlist])
        s = 0
        e = len(string)-1
        print string
        while (s<e) :
            if string[s] != string[e] :
                return False
            s += 1
            e -= 1 
        return True
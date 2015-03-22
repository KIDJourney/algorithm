#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Position: E:\Program\LeetCoder_Python\algorithm\rotate-array.py
# @Author: KIDJourney
# @Email: kingdeadfish@qq.com
# @Date:   2015-03-16
class Solution:
    # @param nums, a list of integer
    # @param k, num of steps
    # @return nothing, please modify the nums list in-place.
    def rotate(self, nums, k):
        temp = nums[:]
        nums = temp[-k:][:] + temp[0:-k][:]
#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Position: E:\Program\LeetCoder_Python\algorithm\test.py
# @Author: KIDJourney
# @Email: kingdeadfish@qq.com
# @Date:   2014-09-25
# nums = [1,2,3,4,5,6,7,8,9]
nums = [1,2]
k = 1
ans = nums[-k:][:] + nums[0:-k][:]
print ans

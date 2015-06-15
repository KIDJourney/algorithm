#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: kidjourney
# @Date:   2015-06-13 12:28:28
# @Last Modified by:   kidjourney
# @Last Modified time: 2015-06-15 23:35:16
import random
nums = [random.randint(1,100) for i in range(20)]
numdict = dict(zip([i for i in range(len(nums))] ,[i for i in nums]))

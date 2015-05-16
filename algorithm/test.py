#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: kidjourney
# @Date:   2015-05-15 16:46:02
# @Last Modified by:   kidjourney
# @Last Modified time: 2015-05-15 17:01:48
mydir1 = {1:10,2:30,3:40}
mydir2 = {1:20,2:20}
mydir = dict(list(mydir2.items())+list(mydir1.items()))
print(mydir)
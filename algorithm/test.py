#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: kidjourney
# @Date:   2015-03-28 21:29:04
# @Last Modified by:   kidjourney
# @Last Modified time: 2015-03-30 21:43:27
binary = bin(1)[2:]
binary = '0'*(32-len(binary)) + binary
print len("00000000000000000000000000000001")
print reverse(binary)
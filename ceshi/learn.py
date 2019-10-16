#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : learn.py
# @Author: hak
# @Date  : 2019-05-29
# @Desc  :
import hashlib

text="CRMForOA@zgg"
text1 = hashlib.md5(text).hexdigest()
print text1



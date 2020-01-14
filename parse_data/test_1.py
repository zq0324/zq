# coding=utf-8
# @FileName: test_1.py
# @Author: ZhengQiang
# Date: 2020/1/8 3:05 下午
import re

s = '/api/1'
res = re.findall('[\d+][,\d+]*', s)
print(res)
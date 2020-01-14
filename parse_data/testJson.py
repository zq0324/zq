# coding=utf-8
# @FileName: testJson.py
# @Author: ZhengQiang
# Date: 2020/1/14 2:02 下午
import json

s = '{"name": "admin", "passwd": "1234"}'
print(type(json.loads(s)))
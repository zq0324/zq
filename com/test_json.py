# coding=utf-8
# @FileName: test_json.py
# @Author: ZhengQiang
# Date: 2020/1/15 5:26 下午
import json
a = "{\"ddd\": {{}}}"

def boyhook(dic):
    print('test')
    if dic['name']:
        return dic['name'], dic['age']
    return dic

new_boy = json.loads(a, object_hook=boyhook)
print(new_boy)
#!/usr/bin/env python
# encoding: utf-8
# @author: cc <chai_pengfei@163.com>

import requests
import re
import os
import json

def get_file(name, page):
    url = 'https://huaban.com/search/?q={name}&k7rejh97&page={page}&per_page=20&wfl=1'.format(name=name, page=page)
    res = requests.get(url)
    regex = r'\[\"pins\"\] = (.*?)];'
    # print(res.text)
    data = re.findall(regex, res.text)
    return json.loads(data[0] + ']')

def get_list(pin):
    url = 'https://huaban.com/boards/58892966?k7zry627&max={}&limit=20&wfl=1'.format(pin)
    # pin = '2453167583'

    res = requests.get(url.format(pin=pin))
    regex = r'\[\"board\"\] = (.*?)};'
    # print(res.text)
    data = re.findall(regex, res.text)
    return json.loads(data[0]+'}')

def download(key, index):
    url = 'https://hbimg.huabanimg.com/{}_fw658'
    res = requests.get(url.format(key))
    with open('images/'+str(index)+'.jpg', 'wb') as f:
        f.write(res.content)
# key_regex = r'key\":\"(.+?)\",'
# keys = re.findall(data[0], key_regex)
# print(keys)
num = 1
pin = '2898541276'
pin_id = ''
page = 1
while num:
    # data = get_file('女 汉服', page)
    # print(data)
    # for d in data:
    #     key = d['file']['key']
    #     download(key, num)
    #     num += 1
    # page += 1
    # if page>20:
    #     break
    data = get_list(pin)
    print(data)
    pins = data['pins']
    for p in pins:
        pin_id = p['pin_id']
        key = p['file']['key']
        download(key, num)
        num += 1
        print(num, key)

    pin = pin_id
    if len(pins) < 20:
        break

# -*-coding:utf-8 -*-
import requests
import json
import time
import xlutils
from xlutils.copy import copy
import xlrd
import re


def write_xls(num, device_num_list):
    book1 = xlrd.open_workbook("device_num_env.xls")
    book2 = copy(book1)

    sheet = book2.get_sheet(0)
    index = 0
    for l in device_num_list:
        sheet.write(num, index, l)
        index += 1
    book2.save("device_num_env.xls")


regex = r'\d+'
url = 'http://{server}.yun-ti.com:8100/api/v2/device/onlinelist'

servers = ["eag-test", "eag-test2"]
headers = {
    'Content-Type': 'application/json',

}
name_list = ['hw']
record = {}
num = 1
monitor_list = ['139615688', '888801', '150561379', '752641570', '139615748',
                '150562323', '139615610', '150561772', '150562100', '139615610']

while 1:
    offline = []
    device_list = []
    run_time = time.strftime("%Y-%m-%d %H:%M:%S")
    tmp = "*" * 20 + "\nRecord time:" + run_time + "\n"
    content = {}
    req = ''
    total, hw_num, real, eag = 0, 0, 0, 0
    for server in servers:
        try:
            req = requests.post(url.format(server=server), headers=headers)
            content = req.json()
        except Exception as e:
            print("Error Info:" + e)
        if req.status_code == 200:
            d_list = content["data"]["deviceOnlineList"]
            total += len(d_list)
            eag = len(d_list)
            # tmp += "total: %s" % total + "\n"

            for i in d_list:
                if i['deviceSerial'].find("hw") >= 0:
                    hw_num += 1
                elif re.findall(regex, i['deviceSerial']):
                    real += 1
                    device_list.append(i['deviceSerial'])

    tmp += "Find HW  device num:%s" % hw_num + "\n"
    tmp += "Find Real  device num:%s" % real + "\n"
    tmp += "Find EAG01  device num:%s" % (total - eag) + "\n"
    tmp += "Find EAG02  device num:%s" % eag + "\n"
    tmp += "Find Total  device num:%s" % total + "\n"
    tmp += "========================\n"
    write_xls(num, [run_time, hw_num, real, total - eag, eag, total])
    print(tmp)
    print("第%s次统计结束。。。。。" % num)
    print("sleep 60 seconds.......")

    num += 1
    time.sleep(10)

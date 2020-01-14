# -*-coding:utf-8 -*-
import requests
import json
import time

url = 'http://eag-test.yun-ti.com:9100/status/getonlinelist'

headers = {
    'Content-Type': 'application/json',

}
name_list = ['zq', 'gong', '00', 'lan']
record={}
while 1:
    tmp = "*"*20+"\nRecord time:"+time.strftime("%Y-%m-%d %H:%M:%S") + "\n"
    content = {}
    req=''
    try:
        req = requests.post(url, headers=headers)
        content = req.json()
    except Exception as e:
        print("Error Info:"+e)
    print('status_code:', req.status_code)
    if req.status_code == 200:
        d_list = content["deviceOnlineList"]
        total = len(d_list)
        tmp += "total: %s" % total + "\n"

        z_num, w_num, g_num, s_num,t_num ,ip_n= 0, 0, 0, 0, 0,0
        for i in d_list:
            if i['deviceSerial'].find("zq") >= 0:
                z_num += 1
            elif i['deviceSerial'].find("lan") >= 0:
                w_num += 1
            elif i['deviceSerial'].find("gong") >= 0:
                g_num += 1
            elif i['deviceSerial'].find("zb") >= 0:
                t_num += 1
            elif i['deviceSerial'].find("su") >= 0:
                s_num += 1
            if i["deviceAddr"].find("0.0.0.0") >= 0:
                ip_n += 1

        tmp += "Find ZQ  device num:%s" % z_num + "\n"
        tmp += "Find Gong  device num:%s" % g_num + "\n"
        tmp += "Find lan  device num:%s" % w_num + "\n"
        tmp += "Find zb  device num:%s" % t_num + "\n"
        tmp += "Find Su  device num:%s" % s_num + "\n"
        tmp += "Other device num:%s" % (total - z_num - g_num - w_num - t_num -s_num) + "\n\n"
        tmp += "Find ip address: 0.0.0.0  device num:%s" % ip_n + "\n"
        tmp += "========================\n"

        print(tmp)
        with open("device.log", "a") as f:
            f.write(tmp)
        print("sleep 60 seconds.......")
        time.sleep(60)


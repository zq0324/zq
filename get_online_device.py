# -*-coding:utf-8 -*-
import requests
import time


url = "http://eag-test.yun-ti.com:8100/status/getbatchdeviceinfo"


while 1:
    run_time = time.strftime("%Y-%m-%d %H:%M:%S")
    tmp = "*" * 20 + "\nRecord time:" + run_time + "\n"

    deviceList = ['150561379', '752641570', '139615748','150562323', '139615610', '150561772','150562100','139615610']
    data = {
        "deviceSerialList": deviceList
    }
    response = requests.post(url, json=data)
    content = response.json()
    device=content["deviceOnlineList"]
    d_list =[]
    for dd in device:    
        d_list.append(dd["deviceSerial"])
        deviceList.remove(dd["deviceSerial"])
    tmp += "online device num: %s ,List:\n%s\n"%(len(device), str(d_list))

    tmp += "offline device Num: %s, List:\n%s \n"%(len(deviceList), str(deviceList))

    tmp+= "="*20

    print(tmp)
    print("waiting for 60s")

    with open("device_env.log", "a") as f:
        f.write(tmp)

    time.sleep(60)

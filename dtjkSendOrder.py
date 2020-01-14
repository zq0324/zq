#!/usr/bin/env python
# -*-coding:utf-8 -*-

import requests
import time
import random

num = 1         #发送计数
allcount = count = 3   #总共发送次数
delay_mix = 1   #延时最小值（秒）
delay_max = 3   #延时最大值（秒）
errorcode_mix = 1000001   #报警编号最小值(1000001~1000019之间)
errorcode_max = 1000019   #报警编号最大值(1000001~1000019之间)

errorcode_mix = errorcode_max = 1000007   #只发送一种告警

url = 'http://120.27.248.33:9110/dt/dtjkSendOrder/insertErrorInfo.do'
liftNo1 = '330108003-0007-0173-2'  #B幢客梯
liftNo2 = '330108003-0007-0670-2'  #A幢货梯
print('#总发送次数：', allcount)
print('#开始计时模拟...')
print('////////////////////////////////////////////////////////////////////////////////////////////////////////////////')
while count:
    errorcode = 1000007
    for errorcode in range(errorcode_mix, errorcode_max+1):
        delaytime = random.randint(delay_mix, delay_max)
        print('#',delaytime,'秒钟后模拟发送报警...')
        time.sleep(delaytime)
        if errorcode == 1000001:
            print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())),'报警编号：',errorcode,'超速')
        if errorcode == 1000002:
            print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())),'报警编号：',errorcode,'震动')
        if errorcode == 1000003:
            print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())),'报警编号：',errorcode,'蹲底')
        if errorcode == 1000004:
            print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())),'报警编号：',errorcode,'冲顶')      
        if errorcode == 1000005:
            print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())),'报警编号：',errorcode,'门区外停梯')
        if errorcode == 1000006:
            print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())),'报警编号：',errorcode,'运行中开门')
        if errorcode == 1000007:
            print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())),'报警编号：',errorcode,'关人无法开门')
        if errorcode == 1000008:
            print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())),'报警编号：',errorcode,'停电故障')
        if errorcode == 1000009:
            print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())),'报警编号：',errorcode,'温度异常')
        if errorcode == 1000010:
            print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())),'报警编号：',errorcode,'遮挡门告警')
        if errorcode == 1000011:
            print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())),'报警编号：',errorcode,'打砸告警')
        if errorcode == 1000012:
            print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())),'报警编号：',errorcode,'一键呼救')
        if errorcode == 1000013:
            print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())),'报警编号：',errorcode,'摄像头服务异常')
        if errorcode == 1000014:
            print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())),'报警编号：',errorcode,'光照异常')
        if errorcode == 1000015:
            print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())),'报警编号：',errorcode,'摄像头遮挡')
        if errorcode == 1000016:
            print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())),'报警编号：',errorcode,'烟雾告警')
        if errorcode == 1000017:
            print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())),'报警编号：',errorcode,'儿童单独进梯')
        if errorcode == 1000018:
            print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())),'报警编号：',errorcode,'逆行告警')
        if errorcode == 1000019:
            print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())),'报警编号：',errorcode,'剧烈运动告警')

        senddata = {'errorTypeCode': errorcode, 'liftNo': liftNo1, 'excuteTime': 1}       #要发送的参数
        r = requests.post(url, data=senddata)                                            #发送报警请求
        print(r.text)
        senddata = {'errorTypeCode': errorcode, 'liftNo': liftNo2, 'excuteTime': 1}
        r = requests.post(url, data=senddata)
        print(r.text)

    print('---------------------------------------------------------------')
    print('#发送完毕!!!')
    print('#总发送次数:',allcount,'次')
    print('#已发送次数:',num,'次')
    print('#剩余发送次数:',count-1,'次')
    print('////////////////////////////////////////////////////////////////////////////////////////////////////////////////')
    num += 1
    count -= 1



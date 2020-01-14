# coding=utf-8
import json
from locust import *

'''
screenid = []
powerid = []
sigid = []

with open("data.json", 'rb') as f:
    rjson = json.load(f)
    el = rjson['Elevs']
    print(len(el))
    for dev in el:
        dd = dev['Devs']
        for d in dd:
            if 'ScrnStaticPrm' in d['Raw']:
                screenid.append(d['Raw']['ScrnStaticPrm']['ScreenMac'])
                # print("num: %s , screen mac: %s" % (len(screenid), d['Raw']['ScrnStaticPrm']['ScreenMac']))
            if 'PwrStaticPrm' in d['Raw']:
                powerid.append(d['Raw']['PwrStaticPrm']['Mac'])
                # print("num: %s , power mac: %s" % (len(powerid), d['Raw']['PwrStaticPrm']['Mac']))
            if 'SigStaticPrm' in d['Raw']:
                sigid.append(d['Raw']['SigStaticPrm']['Mac'])
                # print("num: %s , signal mac: %s" % (len(sigid), d['Raw']['SigStaticPrm']['Mac']))

print("screen: %s" % len(screenid))
print("powerid: %s" % len(powerid))
print("sigid: %s" % len(sigid))
'''



class MyTest(TaskSet):
    def on_start(self):
        self.index = 0

    @task(weight=2)
    def test1(self):
        param = {}
        param["deviceID"] = self.locust.deviceid[self.index]
        self.index = (self.index + 1) % len(self.locust.powerid)
        response = self.client.post(name='get_status', url='/v1/elevator/getStatus', json=param, catch_response=True)
        if response.status_code == 200:
            response.success()
            print("ID:%s  Response: %s" % (param['deviceID'], response.json()))
        else:
            response.failure('error')

    @task(weight=1)
    def getType(self):
        param = {}
        param["powerID"] = self.locust.powerid[self.index]
        self.index = (self.index + 1) % len(self.locust.powerid)
        response = self.client.post(name='get_PowerDevInfo', url='/v1/elevator/power/getDevInfo', json=param, catch_response=True)
        if response.status_code == 200:
            response.success()
            print(response.json())
        else:
            response.failure('error')

    @task(weight=1)
    def setCyc(self):
        param = {}
        param["signalID"] = self.locust.sigid[self.index]
        self.index = (self.index + 1) % len(self.locust.sigid)
        response = self.client.post(name='set_RtStatusCyc', url='/v1/elevator/signal/SetRtStatusCyc', json=param, catch_response=True)
        if response.status_code == 200:
            response.success()
            print(response.json())
        else:
            response.failure('error')


class Run(HttpLocust):
    task_set = MyTest
    host = 'http://192.168.20.4:6520'
    max_wait = 10000
    min_wait = 2000
    screenid = []
    powerid = []
    sigid = []
    with open("data.json", 'rb') as f:
        rjson = json.load(f)
        el = rjson['Elevs']
        for dev in el:
            dd = dev['Devs']
            for d in dd:
                if 'ScrnStaticPrm' in d['Raw']:
                    screenid.append(d['Raw']['ScrnStaticPrm']['ScreenMac'])
                if 'PwrStaticPrm' in d['Raw']:
                    powerid.append(d['Raw']['PwrStaticPrm']['Mac'])
                if 'SigStaticPrm' in d['Raw']:
                    sigid.append(d['Raw']['SigStaticPrm']['Mac'])

    deviceid = screenid + powerid + sigid
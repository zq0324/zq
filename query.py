# -*-coding:utf-8 -*-
import requests
from kafka import KafkaConsumer
import kafka_pb2 as pd
import LiftRtStatus_pb2 as lift
import time
from google.protobuf.json_format import MessageToJson
"""
url_device = 'https://kt-bp.yun-ti.com/basePlatform/lift/querySimpleLiftPage'
header_device = {
    'Content-Type': 'application/json',
    'appCode': 'KFPT',
    'verifyCode': '473ba397-77e6-4cd5-83e8-a0bd23b457ba',
}
data_req = {
    "operatorUserId": "1",
    "pageSize": 10,
    "pageNum": 1,
    "registerCodes": ["954568542315450613", "956878223314562453"]
}
response_device = requests.post(url_device, json=data_req, headers=header_device)
values_device = response_device.json()
data = values_device["data"]["list"]
for dat in data:
    print(dat["liftNo"])
print(data)

"""
groupid = str(int(time.time()))
consumer = KafkaConsumer("pb_yt_time_status_topic", bootstrap_servers="192.168.2.66:9092",group_id=groupid,auto_offset_reset="latest",max_poll_records=10)
print("2124325")
res = consumer.poll(10) 
consumer.seek_to_end()
for msg in consumer:
    proto = pd.LiftRtStatus()
    #proto = pd.LiftRtStatus()
    proto.ParseFromString(msg.value)
    try:
        if proto.dataType == 6 :
            lift_string = lift.Data()
            lift_string.ParseFromString(proto.data)
            print(lift_string)
    except:
        continue
# coding=utf-8
from kafka import KafkaConsumer


consumer = KafkaConsumer("yt_test", bootstrap_servers="192.168.1.48:9092",group_id='TEST',auto_offset_reset='earliest')
print(consumer.offsets())
for msg in consumer:
    print(msg.value.decode())


#coding=utf-8
import socket
import time
import random,string

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # SOCK_STREAM
client.setsockopt(socket.SOL_SOCKET, socket.SO_KEEPALIVE, 1)
try:
    client.connect(('192.168.1.78', 7999))
    while True:
        # msg=''.join(random.sample(string.ascii_letters + string.digits, 10))
        # client.send(msg.encode('utf-8'))
        recv_msg = client.recv(1024)
        print(repr(recv_msg))
        # time.sleep(.51)
except Exception as e:
    print(e)
    client.close()

## 平层感应数据
aa = b'\xaa\xee\x01\x02\x03\x04\x00\t\x00\x0b\x01\x02\x03\x04\x05\x06\x7fo\x80\x02\x01\xa43\x00'
#实时数据
bb = b'\xaa\xee\x01\x02\x03\x04\x00\x07\x00,\x01\x02\x03\x04\x05\x06\x00\x01\x01\x01\x01\x01\x00\xe7\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00y\x00\x0b\x01\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xc43'
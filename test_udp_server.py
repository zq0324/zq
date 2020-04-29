# coding=utf-8
# @FileName: test_udp_server.py
# @Author: ZhengQiang
# Date: 2020/2/26 2:15 下午

import socket
server = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

server.bind(('', 40000))

while 1:
    from_client_data = server.recvfrom(1024)
    if from_client_data:
        print(f"来自{from_client_data[1]}的消息：{from_client_data[0]}")
        # with open('1.flv', 'wb+') as f:
        #     f.write(from_client_data[0])
    # se = input('>>>').encode('utf-8')
    # server.sendto(se,from_client_data[1])
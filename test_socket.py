#coding=utf-8
import socket
import time

def start(ip, port):
    print('start server {0}:{1}'.format(ip, port))
    server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
    server.bind((ip, int(port)))
    server.listen(5)
    try:
        while True:
            conn, address = server.accept()
            print('socket open success')
            print(conn, address)
            while True:
                msg = conn.recv(1024).decode('utf-8')
                if len(msg) == 0:
                    break
                print('recv data ...')
                send_data =  b'\x00\x00\x00(\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x03\x00\x00\x00\x01\x00\x00\x00\x01\x00\x00\x00\x0b\x00\x00\x00\x16\x00\x00\x00\x00'
                if send_data:
                    conn.send(send_data)
                time.sleep(1)
            conn.close()
    except Exception as e:
        print(e)
    finally:
        server.close()

if __name__ == '__main__':
    start('',6666)

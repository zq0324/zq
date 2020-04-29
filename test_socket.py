#coding=utf-8
import socket
import time

def start(ip, port):
    print('start server {0}:{1}'.format(ip, port))
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1)
    server.bind((ip, int(port)))
    server.listen(5)
    try:
        while True:
            conn, address = server.accept()
            print('socket open success')
            print(conn, address)
            num = 1
            data = b''
            while True:
                msg = conn.recv(102400)
                print(msg)
                data += msg
                if len(msg) == 0:
                    break
                # print(data)
                num += 1
                # send_data =  b'\x00\x00\x00(\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x03\x00\x00\x00\x01\x00\x00\x00\x01\x00\x00\x00\x0b\x00\x00\x00\x16\x00\x00\x00\x00'
                # if send_data:
                #     conn.send(send_data)
                time.sleep(1)
            print(data)
            # with open('%s' % num, 'wb') as f:
            #     c = data.split(b'\r\n')
            #     f.write(c[-3])
            conn.close()
    except Exception as e:
        print(e)
    finally:
        server.close()

if __name__ == '__main__':
    start('', 50000)

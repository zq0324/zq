# coding=utf-8
import threading
import time
import requests


class DownThread:
    def __init__(self):
        self._running = True

    def terminate(self):
        self._running = False

    def run(self, n):
        while self._running and n > 0:
            get()
            print(n)
            n -= 1

            #time.sleep(5)


def get():
    url = 'http://192.168.20.4:8081/ehome/780246606?ch=1&streamtype=sub'
    r = requests.get(url, stream=False)
    # print(r.raw.read(200))


c = DownThread()
t = threading.Thread(target=c.run, args=(10,))
t.setDaemon(True)
t.start()
time.sleep(20)
c.terminate()
t.join()

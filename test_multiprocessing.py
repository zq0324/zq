# coding=utf-8
import multiprocessing
import os,time,random

def d(t):
    print("name: %s"%t)
    print("parent_process: %s" % os.getppid())
    time.sleep(10)
    print("process: %s"%os.getpid())


if __name__ == "__main__":
    for i in range(10):
        p = multiprocessing.Process(target=d, args=[i])
        p.start()
        p.join()

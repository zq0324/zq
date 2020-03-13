# coding=utf-8
# @FileName: test-mutiprcs.py
# @Author: ZhengQiang
# Date: 2020/2/18 1:55 下午
import time
import multiprocessing


def f1(i):
    print('muti_a')
    time.sleep(i)


def f2(i):
    print('muti_b')
    time.sleep(i)


if __name__ == '__main__':
    a = multiprocessing.Process(target=f1, args=(10,), name='asd')
    b = multiprocessing.Process(target=f2, args=(15,), name='ppp')
    a.start()
    b.start()
    s = multiprocessing.Semaphore(2)
    print(s)
    print("The number of CPU is:" + str(multiprocessing.cpu_count()))
    for p in multiprocessing.active_children():
        print("child   p.name:" + p.name + "\tp.id" + str(p.pid))


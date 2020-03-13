# coding=utf-8
# @FileName: test_pool.py
# @Author: ZhengQiang
# Date: 2020/2/19 10:05 上午

# coding: utf-8
import multiprocessing
import time

"""
使用进程池，阻塞
"""
def func(msg):
    print("msg:", msg)
    time.sleep(3)
    print("end")
    return "done" + msg


if __name__ == "__main__":
    pool = multiprocessing.Pool(processes=4)
    result = []
    for i in range(4):
        msg = "hello %d" % i
        # pool.apply(func, (msg,))  # 阻塞 维持执行的进程总数为processes，当一个进程执行完毕后会添加新的进程进去
        result.append(pool.apply_async(func, (msg, )))  # 进程池，非阻塞

    print("Mark~ Mark~ Mark~~~~~~~~~~~~~~~~~~~~~~")
    pool.close()
    pool.join()  # 调用join之前，先调用close函数，否则会出错。执行完close后不会有新的进程加入到pool,join函数等待所有子进程结束
    for res in result:
        print(":::", res.get())
    print("Sub-process(es) done.")

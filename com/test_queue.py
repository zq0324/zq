# coding=utf-8
# @FileName: test_queue.py
# @Author: ZhengQiang
# Date: 2020/2/18 4:55 下午

import multiprocessing


def writer_proc(q):
    try:
        print('put fun')
        q.put('sss', block=False)
    except:
        pass


def reader_proc(q):
    try:
        print('get fun')
        print(q.get(block=True))
    except:
        pass


if __name__ == "__main__":
    q = multiprocessing.Queue()
    writer = multiprocessing.Process(target=writer_proc, args=(q,))
    writer.start()

    reader = multiprocessing.Process(target=reader_proc, args=(q,))
    reader.start()

    reader.join()
    writer.join()

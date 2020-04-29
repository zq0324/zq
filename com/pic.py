# coding=utf-8
# @FileName: pic.py
# @Author: ZhengQiang
# Date: 2020/3/11 1:35 下午

import requests
import urllib.parse
import threading

# 设置最大线程锁
thread_lock = threading.BoundedSemaphore(value=10)


# 通过 url 获取数据
def get_page(url):
    page = requests.get(url)
    page = page.content
    # 将 bytes 转化为 字符串
    page = page.decode('utf-8')
    return page
    # print(page)


def pages_from_duitang(label):
    url = 'https://www.duitang.com/napi/blog/list/by_search/?kw={}&start={}&limit=100'
    pages = []
    # 将中文转化成url编码
    label = urllib.parse.quote(label)
    for index in range(0, 3600, 100):
        u = url.format(label, index)
        print(u)
        page = get_page(u)
        pages.append(page)
    return pages


# 一个页面的所有链接
def findall_pages(page, startpart, endpart):
    all_string = []
    end = 0
    while page.find(startpart, end) != -1:
        start = page.find(startpart, end) + len(startpart)
        end = page.find(endpart, start)
        string = page[start:end]
        all_string.append(string)
    return all_string


# 取全部页面
def pic_url_from_pages(pages):
    pic_url = []
    for page in pages:
        url = findall_pages(page, 'path":"', '"')
        pic_url.extend(url)
    return pic_url


def pic_download(url, n):
    r = requests.get(url)
    path = 'pics/' + str(n) + '.jpg'
    with open(path, 'wb')as d:
        d.write(r.content)

    # 下载完了，解锁
    thread_lock.release()


def main(label):
    pages = pages_from_duitang(label)
    pic_url = pic_url_from_pages(pages)
    n = 0
    for url in pic_url:
        n += 1
        print('正在下载第 {} 张图片'.format(n))
        # 上锁
        thread_lock.acquire()
        t = threading.Thread(target=pic_download, args=(url, n))
        t.start()


main('小清新女')
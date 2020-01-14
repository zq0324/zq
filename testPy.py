# coding=utf-8
import traceback
import os,random
import re
import xlrd
import xml.etree.ElementTree as et
import socket
import sys,time
import jsonschema
import docx
import requests
from collections import OrderedDict
import logging
import http.client as http_client
import importlib

a = 'tes'
file_path = './parse_data/test.py'
# lib = __import__('parse_data/'+a+'t.py')
lib = importlib.machinery.SourceFileLoader('t', file_path).load_module()

print(lib.t)
# http_client.HTTPConnection.debuglevel = 1
#
# logging.basicConfig()
# logging.getLogger().setLevel(logging.DEBUG)
# requests_log = logging.getLogger("requests.packages.urllib3")
# requests_log.setLevel(logging.DEBUG)
# requests_log.propagate = True
#
# requests.get('https://www.baidu.com')
#
# ss = OrderedDict([('aa','123'),('a1', 123)])
#
# print(ss.keys())
#


# a='010a000f'
#
# print(int(a,16))
#
# b=67764239
# print(hex(b))
# print(time.perf_counter())
#
# l='\"  123  \"\n\r\"'
# print(l,end='---')
# print(l.strip(' \n\r\"'),end='==')
# print(sys._getframe().f_code.co_filename)
#
# for i in range(200000):
#     ss = i%100000
#     # print(ss)
#     if ss < 10:
#         # ll.append(i)
#         print(i)
#         # n-=1
#     else:
#         n=10
#         ll=[]
# print(time.perf_counter())
#
# def get_cur_info(da):
#     print(sys._getframe().f_code.co_filename ) #当前文件名，可以通过__file__获得
#     print (sys._getframe(0).f_code.co_name)  #当前函数名
#     print (sys._getframe(1).f_code.co_name)#调用该函数的函数的名字，如果没有被调用，则返回<module>，貌似call stack的栈低
#     print (sys._getframe().f_lineno) #当前行号
#     print(sys._getframe(1).f_globals)
#     print(da)
#
# get_cur_info("aa")


# ss = []
# ds = {
#     "ee": ss
# }
#
#
# path = os.path.split(os.path.realpath(__file__))
# print("process %s start" % os.getpid())
# pid = os.fork()
# if pid == 0:
#     print('I am child process (%s) and my parent is %s.' % (os.getpid(), os.getppid()))
# else:
#     print('I (%s) just created a child process (%s).' % (os.getpid(), pid))
# dd = "{0}-10{1:0>5}"
# for n in range(1,11):
#     print(dd.format("mac",n))
#
#
# for i in range(10):
#     ss.append(i)
#
# print(ds)
#
# dd=[{
#     "sn": "128382189"
# },
#     {
#         "sn":"www-zq"
#     }]
#
#
# def fun(n):
#     if n==1:
#         return 1
#     return n+fun(n-1)
#
# d = ["as", "sd","wqe",13]
# print(list.index(d,"sd"))
#
# d[list.index(d,"sd")] = 99999
#
# print(d)
#
# print(fun(4))
#
# ll = "row1-1"
#
# print(ll[3:])
#
# print("显示方式：")
# print("\033[0;37;40m\t方倍实验室\033[0m")
# print("\033[1;37;40m\t方倍实验室\033[0m")
# print("\033[22;37;40m\t方倍实验室\033[0m")
# print("\033[4;37;40m\t方倍实验室\033[0m")
# print("\033[24;37;40m\t方倍实验室\033[0m")
# print("\033[5;37;40m\t方倍实验室\033[0m")
# print("\033[25;37;40m\t方倍实验室\033[0m")
# print("\033[7;37;40m\t方倍实验室\033[0m")
# print("\033[27;37;40m\t方倍实验室\033[0m")
#
# print("前景色：")
# print("\033[0;30;40m\t方倍实验室\033[0m")
# print("\033[0;31;40m\t方倍实验室\033[0m")
# print("\033[0;32;40m\t方倍实验室\033[0m")
# print("\033[0;33;40m\t方倍实验室\033[0m")
# print("\033[0;34;40m\t方倍实验室\033[0m")
# print("\033[0;35;40m\t方倍实验室\033[0m")
# print("\033[0;36;40m\t方倍实验室\033[0m")
# print("\033[0;37;40m\t方倍实验室\033[0m")
#
# print("背景色：")
# print("\033[0;37;40m\t方倍实验室\033[0m")
# print("\033[0;37;41m\t方倍实验室\033[0m")
# print("\033[0;37;42m\t方倍实验室\033[0m")
# print("\033[0;37;43m\t方倍实验室\033[0m")
# print("\033[0;37;44m\t方倍实验室\033[0m")
# print("\033[0;37;45m\t方倍实验室\033[0m")
# print("\033[0;37;46m\t方倍实验室\033[0m")
# print("\033[0;37;47m\t方倍实验室\033[0m")

# regex = r'\d+'
# for d in dd:
#     if re.findall(regex,d['sn']):
#         print('okok')
#         print(d['sn'])
#     else:
#         print(d["sn"])

#
# class A(object):
#     def foo(self):
#         print('A foo')
#
#     def bar(self):
#         print('A bar')
#
#
# class B(object):
#     def foo(self):
#         print('B foo')
#
#     def bar(self):
#         print('B bar')
#
#
# class C1(A,B):
#     pass
#
#
#
# class C2(C1,B):
#     def bar(self):
#         print('C2-bar')
#
#
# class D(C2,B):
#     pass
#
#
# class D1(D):
#     pass
#
#
# class E(D1, C2):
#     def foo(self):
#         print("E's foo")
#
#
# if __name__ == '__main__':
#     print(E.__mro__)
#     d = E()
#     d.foo()
#     d.bar()
#
#
# def o(x):
#     def i(y):
#         nonlocal x
#         x += y
#         return x
#     return i
#
#
# a = o(100)
#
# print(a(12))
# print(a(200))


#
# x=1
# def f1():
#     x=2
#     y=3
#     def f2():
#         print(x)
#         y
#     return f2
# f=f1()                  #f是f2的内存地址
# f()                     #f()就是f2(),可以保证f2()可以在任何位置执行，而不受作用域的限制
# print(f.__closure__)    #打印结果是元组，元组个数代表的是闭包所引用的上次函数的元素个数
# print(f.__closure__[0]) #结果是元组，可以使用索引的方式查看
# print(f.__closure__[1].cell_contents)

#
# try:
#     12/0
# except ZeroDivisionError:
#     traceback.print_exc()

#
# def d(name):
#     def c(func):
#         def b(*args, **kwargs):
#             print("Func :", name)
#             func(*args, **kwargs)
#         return b
#     return c
#
#
# @d("Name D")
# def a(f):
#     print('Func a:', f)


""" 
def swagger_api(url, project, user):
    req = requests.get(url)
    data = req.json()
    apis = data["paths"]
    try:
        params = data["definitions"]
    except KeyError:
        pass
    for api, m in apis.items():
        requestApi = {
            "project_id": project, "status": True, "mockStatus": "200", "code": "", "desc": "",
            "httpType": "HTTP", "responseList": []
        }
        requestApi["apiAddress"] = api
        for requestType, data in m.items():
            requestApi["requestType"] = requestType.upper()
            try:
                requestApi["name"] = data["summary"]
            except KeyError:
                pass
            try:
                if data["consumes"][0] == "application/json":
                    requestApi["requestParameterType"] = "raw"
                else:
                    requestApi["requestParameterType"] = "form-data"
                requestApi["headDict"] = [{"name": "Content-Type", "value": data["consumes"][0]}]
            except KeyError:
                requestApi["requestParameterType"] = "raw"
            for j in data["parameters"]:
                if j["in"] == "header":
                    requestApi["headDict"].append({"name": j["name"].title(), "value": "String"})
                elif j["in"] == "body":
                    dto = j["name"][:1].upper() + j["name"][1:]
                    try:
                        if requestApi["requestParameterType"] == "raw":
                            parameter = {}
                            for key, value in params[dto]["properties"].items():
                                parameter[key] = value['type']
                                requestApi["requestList"] = str(parameter)
                        else:
                            parameter = []
                            for key, value in params[dto]["properties"].items():
                                parameter.append({"name": key, "value": value["type"], "_type": value["tyep"],
                                                  "required": True, "restrict": "", "description": ""})
                            requestApi["requestList"] = parameter
                        # print(requestApi)
                    except:
                        pass
        return requestApi



aa = swagger_api('http://kt-dag.yun-ti.com:6520/swagger-ui/api.swagger.json',12,"321")
print(aa)
"""


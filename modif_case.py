#coding=utf-8
import os

cur = os.path.abspath(os.curdir)
dir_list = os.listdir(cur)
for file in dir_list:
    if file.endswith("txt"):
        print(file)
        tmp = ''
        with open(file,'r') as f:

            for l in f.readlines():
                if l.find("/variable")>=0:

                    tmp += l.replace("/variable", "/lib")
                    print(tmp)
                    print('=================')
                else:
                    tmp += l
        with open(file, 'w') as f:
            f.write(tmp)


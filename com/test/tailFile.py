# -*- coding: UTF-8 -*-

import time
import sys




class readFile:
    def tail(f):
        f.seek(0, 2)
        while True:
            line = f.readline()
            if not line:
                time.sleep(0.5)
                continue
            yield line

    def grep(lines, seText):
        for line in lines:
            if seText in line:
                yield line


'''
try:
    fileName = sys.argv[1]
    targetStr = sys.argv[2]
    
    log = tail(open(fileName))
    for line in grep(log, targetStr):
        print(line)
except Exception as e:
    print("error: %s" % e)
'''

# coding=utf-8
import os
import commands
import time

proc_name = "tuned"
cpu_cmd = "top -b -n 1 | grep %s | awk \'{print $9}\'" % proc_name
mem_cmd = "top -b -n 1 | grep %s | awk \'{print $9}\'" % proc_name

while 1:
    cpu_val =commands.getoutput(cpu_cmd)
    mem_val= commands.getoutput(mem_cmd)
    str1 = "CPU usage: %s"%cpu_val
    str1 += '% \n'
    str1 += "Mem usage: %s"%mem_val
    str1 += '% \n'
    str1 +=  "="*20
    with open("log","a") as f:
        f.write(str1)
    time.sleep(2)



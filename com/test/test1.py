# -*- coding: UTF-8 -*-
import socket  

class Fid:
    def __init__(self,n):
        self.prev = 0
        self.cur = 1
        self.n = n
    def __iter__(self):
        return self
    def __next__(self):
        if self.n > 0:
            value = self.cur
            self.cur +=  self.prev
            self.prev = value
            self.n -= 1
            return value
        else:
            raise StopIteration()


f = Fid(10)
#print([i for i in f])


def fun(n):
    prev,cur = 0, 1
    while n > 0:
        n -= 1
        yield cur
        prev ,cur = cur, cur+prev
        
def read_file(fpath):
    BLOCK_SIZE = 1024
    with open (fpath,'rb') as f:
        while True:
            block = f.read(BLOCK_SIZE)
            if block:
                yield block
            else:
                return
 
       
for i in read_file('11.txt'):
    print(i.decode('gbk'))
    


    
    
'''
for i in fun(10):
    print(i,end = ' ')   
#print(i for i in fun(10))
'''
        

'''
UDP包发送   飞秋协议
udp=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)  
udp.connect(('192.168.1.12',2425))
str =  '1_lbt4_10#32899#002481627512#0#0#0:1289671407:flyingzl:flyingzl:288:一日不见，如三月兮' 
udp.send(str.encode(encoding='utf_8', errors='strict'))  
'''
    
    

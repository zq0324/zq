#-*- coding:utf-8 -*-

import socket,time
import uuid
import hashlib
from websocket import create_connection


svrIp,svrPort = "119.3.21.115",5066
transportType = "WS"
localIp,localPort = "192.168.123.105",27061
uid = "330110002"
passwd = "123456"
g_branch,g_callId =uuid.uuid1(),uuid.uuid1()
host_en = "df7jal23ls0d.invalid"

def getRegHeader(seqNum):
    retStr = "REGISTER sip:{remote_ip} SIP/2.0\r\n"
    retStr += "Via: SIP/2.0/{transport} {host_en};branch={branch}\r\n"
    retStr += "Max-Forwards: 70\r\n"
    retStr += "From: <sip:{uid}@{remote_ip}>;tag={call_number}\r\n"
    retStr += "To: <sip:{uid}@{remote_ip}>\r\n"
    retStr += "Call-ID: {call_id}\r\n"
    retStr += "User-Agent: fs testing\r\n"
    retStr += "CSeq: %d REGISTER\r\n"%seqNum
    retStr += "Contact: sip:{uid}@{host_en}\r\n"
    retStr += "Expires: 60\r\n"
    return retStr

def formatRegHeader(patternStr):
    retstr = patternStr.format(
        remote_ip=svrIp,
        transport=transportType,
        local_ip=localIp,
        local_port=localPort,
        host_en = host_en,
        branch=g_branch,
        uid=uid,
        remote_port=svrPort,
        call_number= uid,
        call_id=g_callId)
    return retstr

class SipRegObj(object):
    def __init__(self,uid,passwd,
        realm="",nonce="",algorithm="MD5",qop="auth"):
        self.uid = uid # "1000"
        self.password = passwd # "1234"
        self.realm = realm
        self.nonce = nonce
        self.algorithm = algorithm
        self.qop = qop
        self.uri = ""
        self.method = "REGISTER"
        self.cnonce = ""
        self.nc = ""
        self.svrIp = svrIp
        #self.transportType = "udp"

    def getReponse(self):
        md5 = hashlib.md5
        ha1 = md5("%s:%s:%s"%(self.uid,self.realm,self.password)).hexdigest()
        ha2 = md5("%s:%s"%(self.method,self.uri)).hexdigest()
        reponse = md5("%s:%s:%s:%s:%s:%s"%(ha1,self.nonce,self.nc,self.cnonce,self.qop,ha2)).hexdigest()
        return reponse

    def getAuthStr(self):
        self.uri,self.cnonce = ("sip:%s"%self.svrIp),uuid.uuid1()
        retStr = ""
        response = self.getReponse()
        retStr += 'Authorization: Digest username="%s",realm="%s",nonce="%s",uri="%s",response="%s",cnonce="%s",nc=%s,qop=%s,algorithm=%s\r\n'%(
            self.uid,self.realm,self.nonce,self.uri,response,self.cnonce,self.nc,self.qop,self.algorithm)
        retStr += 'Content-Length: 0\r\n'
        return retStr

    def genChallengeMsg(self):
        # gen sip reg challenge message
        str1=getRegHeader(1) + "Content-Length: 0\r\n"
        return formatRegHeader(str1)

    def genAuthMsg(self,retstr1):
        # parse data
        data1 = retstr1.split("\r\n")[-4].split(": Digest")[1]
        data1 = str(data1).replace('MD5','"MD5"')
        tmpList = data1.split(",")
        for item in tmpList :
            #print item
            arrtmp = item.split("=")
            setattr(self,arrtmp[0].strip(),arrtmp[1].strip('"'))
        # gen sip reg message with auth
        str2=getRegHeader(2)
        str2 = formatRegHeader(str2)
        str2 += self.getAuthStr()
        return str2

if __name__ == "__main__":

    ws_str = """Upgrade: websocket
Connection: Upgrade
Sec-WebSocket-Protocol: sip
Cache-Control: no-cache
Sec-WebSocket-Key: gRVM91Y7wz/09X1q4r8pAg==
Sec-WebSocket-Version: 13
Sec-WebSocket-Extensions: x-webkit-deflate-frame
User-Agent: Mozilla/5.0 """
    send_str= """REGISTER sip:119.3.21.115 SIP/2.0\r\nVia: SIP/2.0/WS df7jal23ls0d.invalid;branch=z9hG4bK3NWRm5ybdoXTivBx08DAhH21MzikNmZs;rport\r\nFrom: <sip:330101002@119.3.21.115>;tag=bult8AJAc8vgoJIIg1PX\r\nTo: <sip:330101002@119.3.21.115>\r\nContact: "undefined"<sip:330101002@df7jal23ls0d.invalid;rtcweb-breaker=no;transport=ws>;expires=60;click2call=no\r\nCall-ID: bafd5834-2e9e-3a5b-70bd-5be813b5de9a\r\nCSeq: 1 REGISTER\r\nContent-Length: 0\r\nMax-Forwards: 70\r\n"""

    print(send_str)
    treg = SipRegObj(uid,passwd)
    ws =create_connection("ws://119.3.21.115:50020")
    ws.send(ws_str)
    ws.send(send_str)
    result = ws.recv()
    print(result)
    ws.close()
    # client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # #client.bind((localIp,localPort))
    #
    # dstHost = (svrIp,svrPort)
    # client.connect(dstHost)
    # client.send(treg.genChallengeMsg().encode(encoding='utf_8', errors='strict'))
    # print(time.time(),' : send success')
    #
    # # get response (401 msg)
    # retstr1 = client.recv(1024)
    # print(retstr1)
    #
    # client.send(treg.genAuthMsg(retstr1).encode(encoding='utf_8', errors='strict'))
    # print(time.time(),' : send success')
    #
    # retstr2 = client.recv(1024)
    # print("return str : \r\n",retstr2)


# coding=utf-8
import requests
import re

#url = 'http://10.10.0.244:10080/dsp/config/v2/getFrequencyTree'
uri = "http://122.112.251.59:20090"

url = "%s/api/v1/call-account"%uri  #/api/v1/get-account-status?account=330100b002
header = {"content-type": 'application/json; charset=UTF-8',
          "User-Agent":"Mozilla/5.0 ",
          "x-xzl-appkey":  "appkey12"
          }


data = {
  "talktype":1,
  "passwd":"123456",
  "priority":22
}



start = 100000
end = 100001
while start < end:
    aa = format(start, "0>4")
    ac = "3301%s2" % aa
    data["account"] = ac
    response = requests.post(url, json=data, headers=header)
    print(response.status_code, response.json())
    start += 1

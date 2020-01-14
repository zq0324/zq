# coding=utf-8
import requests
import time

uri = "http://122.112.251.59:20090"

url = "%s/api/v1/get-account-status"%uri
header = {"content-type": 'application/json; charset=UTF-8',
          "User-Agent":"Mozilla/5.0 ",
          "x-xzl-appkey":  "appkey12"
          }
data = {}
str_tmp = "{cur_time}, not registered num: {num} detail account list : {account}  \n"

s = requests.session()
while True:
    start = 50
    end = 51
    ac_list = []
    cur_time = time.strftime("%Y-%m-%d %H:%M:%S")
    with open("account.log", 'a') as f:
        while start < end:
            aa = format(start, "0>4")
            ac = "3301%s2" % aa
            data["account"] = ac
            response = s.get(url, params=data, headers=header,timeout=5)
            if response.status_code == 200:
                try:
                    if response.json()["code"] == 0:
                        res_data = response.json()["data"]
                        status = res_data["registered"]
                        if not status :
                            ac_list.append(ac)
                    else:
                        print("error code not eq 0")
                        print(response.text)
                except Exception:
                    continue
            else:
                print(response.status_code)
            start += 1
        tmp = str_tmp.format(cur_time=cur_time,num = len(ac_list), account=ac_list)
        f.write(tmp)
        print(tmp, end="")
    time.sleep(20)
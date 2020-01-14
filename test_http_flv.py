# coding=utf-8
import requests
import random
import string

headers = {
    "User-Agent": "Mozilla/5.0"
}


def get_random_id():
    tmp = random.sample(string.ascii_uppercase, 1)[0]
    num = 1
    while num < 9:
        tmp+= "".join(random.sample(string.digits, 1))# random.sample(string.digits)
        num += 1
    return tmp


# devices=[780246491]

# devices = [228892424, 139615604, 139615558, 780246491, 150562200, 150562391, 780245386, 150560560, 139615556, 656290665, 825307819,780246606, 150561787, 139615589, 150561379, 150561768, 752641570, 139615688]
url = "http://stream-test.yun-ti.com:8080/ehome/{sn}?ch=1&streamtype=sub"
s = requests.session()
server1 = []
server2 = []
num,num1, num2 , num3, num4,num5= 1,0, 0, 0,0,0
# with open("/Users/zhengqiang/PyProjects/eag/device", 'r') as f:
#     devices = eval(f.readline())
# devices = random.sample(range(561730000, 1000000000), 1000)

# for sn in devices:
while num <= 4000:
#     sn = 561730000
#     sn = ''.join(random.sample(string.ascii_uppercase, 1)) + str(sn)
    sn = get_random_id()
    res = s.get(url.format(sn=sn), headers=headers, allow_redirects=False)

    if res.status_code == 302 :
        redirect_url = res.headers["Location"]
        # if redirect_url.find("test.yun-ti.com") >= 0:
        #     num1 += 1
            # server1.append(str(sn))
        if redirect_url.find("122.112.232.202") >= 0:
            num2 += 1

        elif redirect_url.find("119.3.36.59") >= 0:
            num3 += 1
        elif redirect_url.find("test4") >= 0:
            num4 += 1

        else:
            num1 += 1
        #
        # elif redirect_url.find("stream-test3.yun-ti.com") >= 0 :# res.status_code == 404:
        #     num3 += 1
        #
        # elif redirect_url.find("stream-test4.yun-ti.com") >= 0 :# res.status_code == 404:
        #     num4 += 1
        # elif redirect_url.find("stream-test5.yun-ti.com") >= 0 :# res.status_code == 404:
        #     num5 += 1
    print("send device sn: %s" % num)
    num += 1
s.close()
print("重定向到stream-test设备sn：")
print(num1)
print("重定向到122.112.232.202设备sn：")
print(num2)
print("重定向到119.3.36.59设备sn：")
print(num3)
print("重定向到stream-test4设备sn：")
print(num4)
print("重定向到stream-test5设备sn：")
print(num5)
print("===="*100)
# print("重定向到stream-test设备sn 列表：")
# print(", ".join(server1))
# print("重定向到stream-test2 设备sn 列表：")
# print(", ".join(server2))

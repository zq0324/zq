import re, json
import requests

# ss="""{"code":0,"message":"OK","data":[{"registerCode":"$test.registerCode$","liftName":"B座1单元车间1号梯","provinceCode":"330000","cityCode":"330100","townCode":"$test.townCode$","streetCode":"330108003","nbhdName":"格林费尔园区","liftNo":"330108003-0007-0173","floorNum":6,"floorNo":2,"ytStatus":"20","ytStatusName":"正常","onlineStatus":"1","upTime":"2018-05-07 18:36:01"}]}"""

ss = "JSON(application/json)"
#
# start = 'registerCode":"'
# end = '","liftName'
#
# # str_regex = r'{start}(.*?){end}'.format(start=start,end=end)
# str_regex = start + "(.*?)" +end

# str_regex = '(\$.*?\$)'
str_regex = '\((.*?)\)'

print(str_regex)

res = re.findall(str_regex, ss)

print(res)
print("==========")

pp = "{'AppKey': 'soKAM14J7hXQpEVbnBOdYzqUySR9kju5','AppSecret': '3Zd0O6ExyC9mhJUHg4WsDvGSNATBfkKV'}"

# print(eval(pp))
# print(json.loads(pp))
data = {
    'url': 'http://kt-api.yun-ti.com/api/v2/lift/getInfo',
    'method': 'POST',
    'params': {'access_token': 'ad18becb5d9d3c739b7a5a0a6989a251bb42c28b822ab31372127b22cbd38aabca9a91cb5b53a9a8'},
    'headers': {'Content-Type': 'application/json'},
    'json': {
        "registerCodes": ["33010800300070173000", "32201234562018011802"]
    }
}
response = requests.request(**data)

print(response.text)

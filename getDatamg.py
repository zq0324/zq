# coding = utf-8
import requests

url = "http://122.112.243.207:9999/basePlatform/liftequip/getDataManagerIdByHardwareId"

param = {"hardwareId":"B44F960532B8"}

headers = {
    'Content-Type': 'application/json'
}

resp = requests.get(url, headers=headers,params=param)

print(resp.text)
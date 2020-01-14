# coding=utf-8
import json
import xlrd, xlwt
from xlutils.copy import copy
import time


# lines = None
with open("one.log",'r') as f:
    lines = f.readlines()
def write_xls(num, tmp_list):
    book1 = xlrd.open_workbook("realTime.xls")
    book2 = copy(book1)
    sheet = book2.get_sheet(0)
    index = 0
    for l in tmp_list:
        sheet.write(num, index, l)
        index += 1
    book2.save("realTime.xls")

# keys = ['registerNumber', 'speed', 'hasPerson', 'carTemperature', 'carDoorLocked', 'roomTemperature', 'roomDoorLocked', 'pressure', 'carPosition', 'serviceMode', 'carDirection', 'doorZone', 'powerConsumption', 'carOverload', 'faceCount', 'activityMode', 'runModel', 'carDoorModel', 'hallDoorModel', 'machineStatus', 'packageTime','str_time']

keys = ['registerNumber', 'Speed', 'Passenger_Status', 'Car_Temperature', 'Door_Close_Status', 'Machine_Room_Temperature', 'Machine_Room_Door_Status', 'Pressure', 'Car_Position', 'Service_Mode', 'Car_Direction', 'Door_Zone', 'Power_Consumption', 'Car_Overload', 'People_Number', 'Activity_Mode', 'Car_Status', 'Door_Status', 'Histway_Door', 'Lift_Car_Drive_Status', 'Package_Time','str_time']


def write_default(keys):
    book = xlwt.Workbook("realTime.xls")
    sheet = book.add_sheet("realTime")
    index = 0
    for k in keys:
        sheet.write(0,index,k)
        index += 1
    book.save("realTime.xls")

# write_default(keys)  # 新建Excel文档，写入标题信息
index = 1
lift = []
for line in lines:
    devs = json.loads(line)

    for dev in devs:
        if dev["registerNumber"] not in lift:
            lift.append(dev["registerNumber"])
        # if dev["registerNumber"] == "31303101092006040248":
        #     # print(dev.values())
        #     # for k,v in dev.items():
        #
        #     timeStamp = dev["Package_Time"]
        #     # if timeStamp > 1555975223588 :
        #     timeArray = time.localtime(timeStamp/1000)
        #     otherStyleTime = time.strftime("%Y/%m/%d %H:%M:%S", timeArray)
        #     dev["str_time"] = otherStyleTime
        #     write_xls(index,list(dev.values()))
        #     # with open("one_real.log", "a+") as f:
        #     #     f.write(str(dev)+"\n")
        #     print("write excel index: %s......ok"%index)
        #     index += 1
        #     # time.sleep(0.1)
print(lift)
print(len(lift))
""" 
310109010-0701-8274  31303101092006040257
310109010-0701-8284  31303101092006040259 
330108003-0007-1015  31103446022018080001
330302028-2094-4937   311010186201890609
"""

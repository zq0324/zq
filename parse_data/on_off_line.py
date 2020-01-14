# coding=utf-8
# @FileName: on_off_line.py
# @Author: ZhengQiang
# Date: 2020/1/14 8:54 上午
import re, xlsxwriter


# ss = 'time="2020-01-10T03:26:53+08:00" level=info msg="ehome相机成功下线:' \
#      ' 序列号:224466049; 内网地址[172.18.0.10:9165]; 外网地址[36.24.212.166:9165]; UserID:113216;' \
#      ' ehomedeviceCnt:77685"'
# s1 = 'time="2020-01-10T03:26:53+08:00" level=info msg="ehome相机成功下线: 序列号:D83296537; 内网地址[172.18.0.10:9531]; 外网地址[117.174.84.27:9531]; UserID:116241; ehomedeviceCnt:77680"'
# time_s = re.findall('time="(\S+)"',ss)
# t2 = re.findall('time="(\S+)"', s1)
# d1 = re.findall('序列号:(\w+);', s1)
# print(time_s)
# print(time_s[0] == t2[0])
# print(d1)
# dd = ['d222','c3324','5','c3324']
# print(list(set(dd)))

def write_excel(data, name):
    workbook = xlsxwriter.Workbook('%s.xlsx' % name)
    sheet1 = workbook.add_worksheet()
    index = 0
    # start_k = 0
    for k in sorted(data.keys()):
        # print(type(k))
        # if not start_k:
        #     start_k = k
        sheet1.write(index, 0, k)
        sheet1.write(index, 1, data[k])
        index += 1
    workbook.close()


def get_line(name):
    with open('{}.txt'.format(name), 'r', encoding='utf-8') as f:
        for line in f.readlines():
            yield line


def get_data(name):
    data = {}
    device_list = []
    t0 = ''
    for line in get_line(name):
        try:
            t1 = re.findall('time="(\S+)"', line)[0]
            device = re.findall('序列号:(\w{9})', line)[0]
        except IndexError:
            print(re.findall('序列号:(\w{9})', line))
            continue
        # print(device)
        if t0 == '':
            t0 = t1
            device_list.append(device)
            continue
        if t0 == t1:
            device_list.append(device)
        else:
            data[t0] = len(set(device_list))
            data[t1] = 1
            device_list = [device]
            t0 = t1
    return data


file = '上线'
data = get_data(file)
write_excel(data, file)
# print(data)

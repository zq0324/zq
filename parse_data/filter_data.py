# coding=utf-8
# @FileName: filter_data.py
# @Author: ZhengQiang
# Date: 2019/12/27 10:19 上午
import re
import xlsxwriter
import numpy as np
from matplotlib import pyplot as plt
from matplotlib.ticker import MultipleLocator, Locator

def get_data(time,end):
    with open('zq.txt', 'r') as f:
        status = False
        for line in f.readlines():
            if line.find(time) > 0:  # or line.find(end) > 0:
                status = True
            if line.find(end) > 0:
                status = False
            if status:
                yield line


def filter_data():
    time_stamp={}
    for line in get_data('2019-12-26T17:00', '2019-12-26T18:04'):
        key = re.findall('\d{10}', line)[1]
        if key in time_stamp.keys():
            time_stamp[key] += 1
        else:
            time_stamp[key] = 1
    return time_stamp

def cp_new(data):
    key = '1577350757'
    tmp = data.copy()
    while 1:
        if key not in data.keys():
            print('999999999')
            tmp[key] = 0
            key = str(int(key)+1)
        else:
            key = str(int(key)+1)
        if key == '1577354601':
            break
    return tmp


def write_excel(data):
    workbook = xlsxwriter.Workbook('data.xlsx')
    sheet1 = workbook.add_worksheet()
    index = 0
    start_k = 0
    for k in sorted(data.keys()):
        # print(type(k))
        if not start_k:
            start_k = k
        sheet1.write(index, 0, k)
        sheet1.write(index, 1, data[k])
        index += 1
    workbook.close()

# def chart_data(data):
#     # 创建x,y轴标签
#     plt.style.use('ggplot')  # 设置绘图风格
#     fig = plt.figure(figsize=(10, 6))  # 设置图框的大小
#     ax1 = fig.add_subplot(1, 1, 1)
#     data.plot()  # 绘制折线图
#     x = np.arange(0, len(data), 1)
#     ax1.plot(x, data.values,  # x、y坐标
#     color = '#C42022',  # 折线图颜色为红色
#     marker = 'o', markersize = 4  # 标记形状、大小设置
#     set_xticks(x)  # 设置x轴标签为自然数序列
#     ax1.set_xticklabels(data.index)  # 更改x轴标签值为年份
#     plt.xticks(rotation=90)  # 旋转90度，不至太拥挤
#     for x, y in zip(x, data.values):
#         plt.text(x, y + 10, '%.0f' % y, ha='center', color=colors1, fontsize=10)
#
#     plt.title('历年中国内地上市公司数量变化', color=colors1, fontsize=18)
#     plt.xlabel('年份')
#     plt.ylabel('数量(家)')
#
#     plt.show()
#
write_excel(cp_new(filter_data()))
# print(len(filter_data()))
#coding=utf-8

import xlrd

readbook = xlrd.open_workbook('device_num_env.xls')
sheet = readbook.sheet_by_name('sheet1')
for i in range(sheet.nrows):
    print(sheet.row_values(i))
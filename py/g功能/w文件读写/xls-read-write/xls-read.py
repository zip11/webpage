#!/usr/bin/python3
# -*- coding: UTF-8 -*-

import xlrd

data = xlrd.open_workbook('test.xls') # 打开xls文件

table = data.sheets()[0] # 打开第一张表

nrows = table.nrows # 获取表的行数

# 循环逐行输出

for i in range(nrows): 

   if i == 0: # 跳过第一行

       continue

   print (table.row_values(i)[:13]) 
   # 取前十三列数据
#!/usr/bin/python3
# -*- coding: UTF-8 -*-

# xls add value

import xlrd
from xlutils.copy import copy

fpath='mcw_test.xls'

valueli=[["3","明明如月","女","听歌","2030.07.01"],
         ["4","志刚志强","男","学习","2019.07.01"],]

def write_excel_xls_append(path, value):

    index = len(value)  
    # 获取需要写入数据的行数

    workbook = xlrd.open_workbook(path)  
    # 打开工作簿
    sheets = workbook.sheet_names()  
    # 获取工作簿中的所有表格

    worksheet = workbook.sheet_by_name(sheets[0])  
    # 获取工作簿中所有表格中的的第一个表格
    rows_old = worksheet.nrows  
    # 获取表格中已存在的数据的行数

    new_workbook = copy(workbook)  
    # 将xlrd对象拷贝转化为xlwt对象
    new_worksheet = new_workbook.get_sheet(0)  
    # 获取转化后工作簿中的第一个表格

                    #行 数
    for i in range(0, index):
                        #列 数
        for j in range(0, len(value[i])):
                                #行 ，列 ， value
            new_worksheet.write(i+rows_old, j, value[i][j])  
            # 追加写入数据，注意是从i+rows_old行开始写入

    new_workbook.save(path)  
    # 保存工作簿

    print("xls/xlsx格式表格【追加】写入数据成功！")

write_excel_xls_append(fpath,valueli)
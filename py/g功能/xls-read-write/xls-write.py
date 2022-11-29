#!/usr/bin/python3
# -*- coding: UTF-8 -*-

# write xls

import xlwt

# 创建一个workbook并设置编码
workbook = xlwt.Workbook(encoding = 'utf-8')

# 添加sheet
worksheet = workbook.add_sheet('微课列表')

# 写入excel, 参数对应 行, 列, 值
worksheet.write(1,0, label = 'MySQL零基础入门课程')

# 保存
workbook.save('W3Cschool课程内容.xls')

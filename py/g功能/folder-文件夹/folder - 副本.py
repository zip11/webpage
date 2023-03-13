#!/usr/bin/python
# -*- coding: UTF-8 -*-

# 遍历文件夹

import os

# 搜索文件夹
lj1 = r"C:\Users\\Downloads"

# 图片文件夹 列表
ncpt_folder = []

# 遍历文件夹
for root, dirs, files in os.walk(lj1, topdown=False):

    # 文件 遍历
    # for name in files:
    #     print(os.path.join(root, name))


    # 文件夹 遍历
    for name in dirs:
        
        # print(os.path.join(root, name))  

        #判断文件夹 名字 存在 picnc
        if(name.find("picnc") != -1):
            
            # list 添加 文件夹 元素
            ncpt_folder.append(name)
            
print("图片文件夹_列表:",ncpt_folder)
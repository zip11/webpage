#!/usr/bin/python3
# -*- coding: UTF-8 -*-

# move *.flv to xz folder ,linux

import os
from os import path
# move file
import shutil

# 当前 文件夹 路径
ljqd = ""

#xz 文件夹路径
ljxz = ""

# list index 
wz1 = 0



# 获取文件路径，获取文件名称列表
lj1 = os.getcwd()

#格式化路径的格式
source = path.normpath(lj1)

#获取 目录 文件
videoList = os.listdir(source)

# 只选择目录下的 flv 文件
for Sname in videoList:

    #判断字符串是否以指定后缀结尾
    if not Sname.endswith("flv"):

        #remove() 函数用于移除列表中某个值的第一个匹配项
        videoList.remove(Sname)

#获取 当前 文件夹
ljqd =os.getcwd()

#生成 flv 绝对路径
for  flvfile in videoList:

    #元素 位置
    wz1 = videoList.index(flvfile)

    # 替换 元素 ，绝对路径
    videoList[wz1] = os.path.join(ljqd,flvfile)


#组合 xz 文件夹 路径
ljxz = os.path.join(ljqd,'xz')

#print(videoList)

# move flv to xz folder

for i in videoList:
    shutil.move(i,ljxz)    

print("flv to xz folder end !!! ")



#!/usr/bin/python3
# -*- coding: UTF-8 -*-

#flv to mp4 ,ffmpeg ,linux

import os
from os import path

# 获取文件路径，获取文件名称列表
lj1 = os.getcwd()

#格式化路径的格式
source = path.normpath(lj1)

#获取 目录 文件
videoList = os.listdir(source)

# 只选择目录下的mkv文件
for Sname in videoList:

    #判断字符串是否以指定后缀结尾
    if not Sname.endswith("flv"):

        #remove() 函数用于移除列表中某个值的第一个匹配项
        videoList.remove(Sname)

# 执行ffmpeg命令
for i in videoList:
    
    #文件名 不含 后缀
    output = i[0:-4]

    #flv to mp4 命令
    cmd = 'ffmpeg -i "%s/%s" -c:v copy -c:a copy "%s/%s.mp4"' %(lj1,i,lj1,output)
    os.system(cmd)

    #delete flv
    os.remove(i)
    print("delete flv ok")

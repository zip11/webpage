#!/usr/bin/python3
# -*- coding: UTF-8 -*-

#mp4 to aac ,ffmpeg ,linux

import os
from os import path

# aac file list
aaclist = []

print('mp4 to aac,ffmpeg')
os.system('pause')


# 获取文件路径，获取文件名称列表
lj1 = os.getcwd()

#格式化路径的格式
source = path.normpath(lj1)

#获取 目录 文件
videoList = os.listdir(source)

# 只选择目录下的mp4文件
for Sname in videoList:

    #判断字符串是否以指定后缀结尾
    print('mp4:',Sname.endswith("mp4"))
    if  Sname.endswith("mp4"):


        aaclist.append(Sname)

print('videolist:',videoList)

# 执行ffmpeg命令
for i in videoList:
    
    #文件名 不含 后缀
    output = i[0:-4]

    #flv to mp4 命令
    cmd = 'ffmpeg -i "%s/%s"  -c:a copy "%s/%s.aac"' %(lj1,i,lj1,output)

    print('cmd :',cmd)
    os.system(cmd)
    os.system('pause')

    #delete flv
    #os.remove(i)
    print("delete mp4 ok")

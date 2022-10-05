#!/usr/bin/python3
# -*- coding: UTF-8 -*-

# aac to m4a ,rename

import os
from os import path

# aac file list
aaclist = []

print('rename  aac to m4a')
#os.system('pause')



# 获取py文件， 所在 文件夹 路径
lj1 = os.path.dirname(os.path.abspath(__file__))

#格式化路径的格式
source = path.normpath(lj1)

#获取 目录 文件
videoList = os.listdir(source)

# 只选择目录下的flv文件
for Sname in videoList:

    #判断字符串是否以指定后缀结尾
    print('aac:',Sname.endswith("aac"))
    if  Sname.endswith("aac"):


        aaclist.append(Sname)

print('aaclist:',aaclist)

# 执行ffmpeg命令
for i in aaclist:

    # aac 绝对路径
    ljaac = os.path.join(lj1,i)
    
    # 文件名 不含 后缀~~~~~~~
    ljm4a = i[0:-4]
    # 合成 m4a
    ljm4a = ljm4a + ".m4a"

    # m4a绝对路径
    ljm4a = os.path.join(lj1,ljm4a)

    #重命名 为 m4a
    os.rename(ljaac,ljm4a)
    # M4A END ~~~~~~~~~


    #  mp4 绝对路径~~~~~~~~~~~
    ljmp4 = i
    ljmp4 = os.path.join(lj1,ljmp4)

    # remove mp4 file
    os.remove(ljmp4)
    # mp4 end~~~~~~~~~~~~

    print("aac to m4a")

print("\n<<< end >>>")

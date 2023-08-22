#!/usr/bin/python3
# -*- coding: UTF-8 -*-

#flv to aac ,ffmpeg ,linux

import os
from os import path

import sys

def renaming(file):

    print("rename aac path:",file)
    
    """修改后缀"""
    ext = os.path.splitext(file)    # 将文件名路径与后缀名分开

    if ext[1] == '.aac':                    # 文件名：ext[0]
        new_name = ext[0] + '.m4a'         # 文件后缀：ext[1]
        os.rename(file, new_name)           # tree()已切换工作地址，直接替换后缀

# aac file list
aaclist = []

# 搜索指定  MP4
hzname = "flv"

print(hzname + ' to aac,ffmpeg')

# cmd 参数
lj1 = sys.argv[1]

# 获取py文件， 所在 文件夹 路径
# lj1 = os.path.dirname(os.path.abspath(__file__))

# exe获取 目录
# lj1 = os.getcwd()

print("py file:",lj1)

os.system('pause')

#格式化路径的格式
source = path.normpath(lj1)

#获取 目录 文件
videoList = os.listdir(source)

# 只选择目录下的flv文件
for Sname in videoList:

    #判断字符串是否以指定后缀结尾
    print(hzname  + ':',Sname.endswith(hzname))
    if  Sname.endswith(hzname):


        aaclist.append(Sname)

print('aaclist:',aaclist)

# 执行ffmpeg命令
for i in aaclist:
    
    #文件名 不含 后缀
    v_path = os.path.splitext(i)  
    output = v_path[0]

    # 新 音频文件名
    audio_name = output + ".aac"
    # 全路径 视频
    full_video_path = os.path.join(lj1,i)
    # 全路径 音频
    full_audio_path = os.path.join(lj1,audio_name)
    
    #flv to flv 命令
    cmd = 'ffmpeg -i "%s"  -c:a copy "%s"' %(full_video_path,full_audio_path)

    print('cmd :',cmd)
    os.system(cmd)
    
    #os.system('pause')

    # 重命名 m4a
    # os.system("rename 's/\.aac/\.m4a/'  *")
    
    renaming(full_audio_path)

    #delete flv

    #flv绝对路径
    i = os.path.join(lj1,i)
    os.remove(i)
    
    print("delete "+ hzname + " ok")

print("\n<<< end >>>")

os.system("pause")

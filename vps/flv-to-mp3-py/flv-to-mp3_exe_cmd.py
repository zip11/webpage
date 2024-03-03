#!/usr/bin/python3
# -*- coding: UTF-8 -*-

#flv to aac ,ffmpeg ,linux

import os
from os import path

import sys



# aac file list
aaclist = []

# 搜索指定  MP4
hzname = "flv"

print(hzname + ' to mp3,ffmpeg')
print("flv转mp3，保持原始采样率，单声道，vbr是128k")

# cmd 参数
lj1 = sys.argv[1]

# 获取py文件， 所在 文件夹 路径
# lj1 = os.path.dirname(os.path.abspath(__file__))

# exe获取 目录
# lj1 = os.getcwd()

print("py file:",lj1)

# os.system('pause')

#格式化路径的格式
source = path.normpath(lj1)

#获取 目录 文件
videoList = os.listdir(source)

# 只选择目录下的flv文件
for Sname in videoList:

    #判断字符串是否以指定后缀结尾
    print(hzname  + ' has :',Sname.endswith(hzname))
    if  Sname.endswith(hzname):


        aaclist.append(Sname)

print('video-file-list:',aaclist)

# 执行ffmpeg命令
for i in aaclist:
    
    # 分割 文件名，
    v_path = os.path.splitext(i)
    #文件名 不含 后缀
    output = v_path[0]

    # 新 音频文件名
    audio_name = output + ".mp3"
    # 全路径 视频
    full_video_path = os.path.join(lj1,i)
    # 全路径 音频
    full_audio_path = os.path.join(lj1,audio_name)
    
    # flv to mp3命令
    cmd = 'ffmpeg -i "%s" -vn -acodec libmp3lame -q:a 4 -ac 1  "%s"' %(full_video_path,full_audio_path)

    print('cmd :',cmd)

    # ffmpeg 运行
    os.system(cmd)
    
    #delete flv
    os.remove(full_video_path)
    
    print("delete "+ hzname + " ok")


print("\n<<< video to audio end >>>")


# os.system("pause")

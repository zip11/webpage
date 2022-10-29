#!/usr/bin/python3
# -*- coding: UTF-8 -*-

#flv to aac ,ffmpeg ,linux

import os
from os import path
import sys

# *.aac rename *.m4a
def gname(wlj):

    # 列出当前目录下所有的文件
    files = os.listdir(wlj)  
    
    # 如果path为None，则使用path = '.' 

    for filename in files:

        portion = os.path.splitext(filename)  
        # 分离文件名与扩展名
        
        # 如果后缀是jpg
        if portion[1] == '.aac':

            # 重新组合文件名和后缀名
            newname = portion[0] + '.m4a'
            os.chdir(wlj)
            os.rename(filename, newname)



# aac file list
aaclist = []

print('flv to aac,ffmpeg')

# 获取py文件， 所在 文件夹 路径
#lj1 = os.path.dirname(os.path.abspath(__file__))

# exe获取 目录
#lj1 = os.getcwd()

# cmd 参数
lj1 = sys.argv[1]

print("py file:",lj1)

os.system('pause')

#格式化路径的格式
source = path.normpath(lj1)

#获取 目录 文件
videoList = os.listdir(source)

# 只选择目录下的flv文件
for Sname in videoList:

    #判断字符串是否以指定后缀结尾
    print('flv:',Sname.endswith("flv"))
    if  Sname.endswith("flv"):


        aaclist.append(Sname)

print('aaclist:',aaclist)

# 执行ffmpeg命令
for i in aaclist:
    
    #文件名 不含 后缀
    output = i[0:-4]

    #flv to flv 命令
    cmd = 'ffmpeg -i "%s/%s"  -c:a copy "%s/%s.aac"' %(lj1,i,lj1,output)

    print('cmd :',cmd)
    os.system(cmd)
    
    #os.system('pause')


    #os.system("rename 's/\.aac/\.m4a/'  *")



    #delete flv

    #flv绝对路径
    i = os.path.join(lj1,i)
    # del flv
    os.remove(i)
    
    print("delete flv ok")


# *.aac  rename *.m4a

gname(lj1)
print("aac rename m4a ok")

print("\n<<< end >>>")

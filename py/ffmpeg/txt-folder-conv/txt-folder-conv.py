#!/usr/bin/python3
# -*- coding: UTF-8 -*-

# 读取txt每行命令，转换多个文件夹 flv to aac

import os

f=open('folder.txt','r')
 
lines=f.readlines()  
#读取整个文件所有行，保存在 list 列表中
 
for line in lines:
    
    line=line.replace("\n","")
    # del \n

    print("flv-foler:"+line)

    fml = "./flv-to-aac-cmd.py  \"" + line + '"'
    # run  py
     
    os.system(fml)


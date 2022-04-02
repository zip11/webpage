#!/usr/bin/python
# -*- coding: UTF-8 -*-

#获取 子文件夹 图片 转换 webp 存入 相同名字 新文件夹
# webp 95 压缩质量

import os



#旧图片 根文件夹 

lj1 = input("input jpg folder ")

#输入图片 高度 降低数字，
tpgd = input("jpg hegiht/2 , default  number 2 ")

#图片 高度/2
if tpgd == "":
    tpgd = "2"


print(lj1)

#字符串前面加r，表示原始字符

#子文件夹 列表
zwjj = []


#根文件夹 名字 ，非完整 路径
gwjj1 = os.path.basename(lj1)
gwjj1 = gwjj1 + 'webp'


#根路径 上一层 文件夹
glj = os.path.dirname(lj1)

ngml = os.path.join(glj,gwjj1)

#新建 文件夹根目录
os.mkdir(ngml)


for root, dirs, files in os.walk(lj1, topdown=False):

#获取 子文件夹
    for name in dirs:
        #            根目录 + 子文件夹 名字
         zwjj.append(os.path.join(root, name))

#显示 子文件夹 列表
print(zwjj)

#判断 是 单个文件夹  
if len(zwjj) == 0 :
    zwjj.append(lj1) 


for zwj in zwjj:
    
    #zwj 子文件夹 完整路径

    #获取 子文件夹 下 图片文件名
    ztps = os.listdir(zwj)

    #子文件夹 名字 ，非完整 路径
    nwjj2 = os.path.basename(zwj)

    #新文件夹
    nwjj1 = os.path.join(ngml,nwjj2)

    

    #创建 webp目录
    os.mkdir(nwjj1) 

    for tp in ztps:
        
        #子文件夹 转换 单个 图片


        #新 图片 文件名
        ntp1 =  '"' + nwjj1 + os.path.sep + os.path.splitext(tp)[0] + ".webp" +  '"' 

        #旧图片 子文件夹路径 + 图片名字
        oldtp1 = os.path.join(zwj,tp)

        #旧图片路径 加 "
        oldtp1 = '"' + oldtp1 + '"'

        #ffmpeg命令
        ml1 = "ffmpeg -i " + oldtp1 + "  -vf scale=-1:ih/" + tpgd +" -preset   picture -quality 95  " + ntp1
        
        print(ml1)
        
        #cmd 运行 ffmpeg
        os.system(ml1)


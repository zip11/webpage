#old video
#1文件名 中 删除中文 
#2 abc123.mp4,add '-'

#abc123.mp4,abc最少是3个

#提取视频文件名中， 英文字符串，改名字为英文 文件名
#aaa-123测试.mp4  -> aaa-123.mp4

import os
import re

def gm(src,dst):

    #文件名字  改名
    try:

        #纯英文 不用改名
        if(src != dst):
        
            print('dst',dst)
            os.rename(src, dst)
            print('rename file success\r\n')
       
    except Exception as e:
        print(e)
        print('rename file fail\r\n')



print("rename 去除视频文件名 中的 中文字符串\n")

#exe 当前目录
filePath = './'

#获取 目录 列表
files = os.listdir(filePath)

print(files)

#删除 中文
for file in files:

    try:
        str = file

        #del chinese NUM 1,2
        zfc = re.sub('[\u4e00-\u9fa5]{1,2}', '', str)

        nwjm = zfc

        #rename file
        gm(file,nwjm)
    except:
        
        continue

#获取 目录 列表
files = os.listdir(filePath)

for file in files:

    try:
        str = file

        # abc123.mp4
        zfc = re.findall(r"([A-Za-z]{2,5})(\d{3,4}).*(.mp4|.mkv|.avi)",str)
        
        # 放入list,自动分割
        xwjm = zfc[0]

        #拼接 新 文件名 ,ADD '-'
        nwjm = xwjm[0] + '-' + xwjm[1] + xwjm[2]
        gm(file,nwjm)
    except:
        
        continue

os.system('pause')




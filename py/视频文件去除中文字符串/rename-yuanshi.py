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
       
    except Exception as e:
        print(e)
        print('rename file fail\r\n')
    else:
        print('rename file success\r\n')


print("rename 去除视频文件名 中的 中文字符串\n")

#exe 当前目录
filePath = './'

#获取 目录 列表
files = os.listdir(filePath)

print(files)

for file in files:

    try:
        str = file
        zfc = re.findall(r".*([A-Za-z]{3,5}-\d{3,4}).*(.mp4|.mkv|.avi)",str)
        
        # 放入list,自动分割
        xwjm = zfc[0]

        #拼接 新 文件名
        nwjm = xwjm[0]+xwjm[1]
        gm(file,nwjm)
    except:
        
        continue


os.system('pause')




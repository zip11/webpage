#!/usr/bin/python3
import requests
import os

#修改文件
def err_num(num):
    #打开一个文件只用于写入。如果该文件已存在则打开文件，并从开头开始编辑，即原有内容会被删除。如果该文件不存在，创建新文件。
    fo = open("err_num.txt","w")
    #转换为字符串
    num = str(num)
    #fo = open("D:/temp/123.txt","w")
    fo.write(num)
    #关闭文件
    fo.close()

#获取输入参数
try:
    #请求百度
    r = requests.get('https://www.baidu.com/',timeout=10)
    code = r.status_code
except:
    code = -1
    pass

if( code >= 200 ):
    err_num('0')
else:
    #读取当前错误次数
    fo = open("err_num.txt","r")
    num = fo.read()
    #重置次数为0
    if ( num == '' ):
        num = 0
    fo.close()
    #当前错误次数+1
    num = int(num) + 1
    #print(num)

    err_num(num)
    if( num >= 5 ):
        #执行关机操作
        os.system('shutdown -s now')
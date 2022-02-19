#!/usr/bin/env python3 
# -*- coding: utf-8 -*-

import urllib3
from ftplib import FTP
import time
import tarfile
import os


def ftpconnect(host,port, username, password):
    ftp = FTP()
    # ftp.set_debuglevel(2)
    ftp.connect(host, int(port))
    ftp.login(username, password)
    ftp.set_debuglevel(2) 
    return ftp

#从ftp下载文件
def downloadfile(ftp, remotepath, localpath):
    bufsize = 1024
    fp = open(localpath, 'wb')
    ftp.retrbinary('RETR ' + remotepath, fp.write, bufsize)
    ftp.set_debuglevel(0)
    fp.close()

#ftp上传文件
def uploadfile(ftp, remotepath, localpath):
    bufsize = 1024
    fp = open(localpath, 'rb')

    print("txt up",fp)

    ftp.storbinary('STOR ' + remotepath, fp, bufsize)
    ftp.set_debuglevel(0)
    fp.close()

#上传 txt 文本文件
def uploadtxt(ftp, remotepath, localpath):

        ftp.set_debuglevel(1)

        with open(localpath, 'rb') as fp:

            res = ftp.storlines("STOR " + remotepath, fp)

            if not res.startswith('226 Transfer complete'):

                print('Upload failed')
            
            ftp.set_debuglevel(0)
            





#外网ip 写入 txt
def txtwr(lj1,wz3):

    file = open(lj1, 'w')
    file.write(wz3)
    file.close()

#生成 ip 的html网页
def htmlwr(lj2,wz3):

    file = open(lj2, 'w')
    
    wz3 = "<!DOCtype HTML>\
    \n<head><title>新的网页</title></head>\
    \n<body><h1>" + wz3 + "</h1></body>"
    
    file.write(wz3)
    file.close()   

#读取txt内容
def txtread(path):
    #
    wj = open(path, 'r')
    nr = wj.read()
    
    wj.close( )
    return nr



if __name__ == "__main__":

    txtlj = "/run/user/1000/ip.txt"
    htmllj = "/run/user/1000/ip.html"
    
    ftpip = ""
    ftpport =
    ftpna = "
    ftpmm = "

    http = urllib3.PoolManager()

    #发起一个GET请求并且获取请求的响应结果
    r = http.request('GET', 'http://ifconfig.me')

    #输出响应的数据
    print(r.data)

    ip1 = r.data

    #byte转换 str
    ip2 = ip1.decode('utf-8')
    print(ip2)

    #保存 外网ip 到txt
    txtwr(txtlj,ip2)

    wz4 = txtread(txtlj)
    print("txt read ip",wz4)

    #写出 html ip
    htmlwr(htmllj,ip2)



    #连接 登录 ftp
    ftp = ftpconnect(ftpip,ftpport, ftpna, ftpmm)
    
    #上传公网 ip.txt
    uploadtxt(ftp,"ip.txt",txtlj)

    uploadtxt(ftp,"ip.html",htmllj)

                    #ftp路径 ， 本地txt

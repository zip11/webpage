#!/usr/bin/python3
# -*- coding: UTF-8 -*-

# 下载文件

import requests

proxy1 = ''


# 下载文件
def download_tor(wz_tor,tor_file,proxy):

    print("下载文件")

    proxies = {
        "http": "socks5://%(proxy)s/" % {'proxy': proxy},
        "https": "socks5://%(proxy)s/" % {'proxy': proxy}
    }

    # 下载链接
    r = requests.get(wz_tor,proxies=proxies)

    # 保存文件
    with open(tor_file, "wb") as f:
        f.write(r.content)
        
    print("下载完成")






from flask import Flask,request,render_template

import flask

import re

app = Flask(__name__)

@app.route('/api/get')

def testGet():
    
    # 下载文件 网址
    name = request.args.get('name')

    # 下载文件 名字
    t_file = request.args.get('title')

    # 删除 [] 内容
    t_file = re.sub(r'\[.*\]',"",t_file)
    # 加 种子 后缀 
    t_file = t_file + ".torrent"

    print("Link:  \n",name,"\n")

    print("start-proxy-torrent!!!")
    
    download_tor(name,t_file,proxy1)

    print("end-proxy-torrent!!!")

    return render_template("index.html",name=name,t_file=t_file,proxy1=proxy1) 
    # 作者：热心的裴同学 https://www.bilibili.com/read/cv5129517/ 出处：bilibili
    
    # return "get方法获取参数: \" {}  filename : {} \" ".format(name,t_file) 

if __name__ == '__main__':
    app.run(debug=True)
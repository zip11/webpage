#!/usr/bin/python3
# -*- coding: UTF-8 -*-

# 下载文件

import requests

print("下载文件")

# 输入网址
wz_tor = "" 
wz_tor = input("input file link:")

proxy = '192.168.2.1:111'

proxies = {
    "http": "socks5://%(proxy)s/" % {'proxy': proxy},
    "https": "socks5://%(proxy)s/" % {'proxy': proxy}
}

# 下载链接
r = requests.get(wz_tor,proxies=proxies)

filename = "1.torrent.jpg"

# 保存文件
with open(filename, "wb") as f:
    f.write(r.content)
    
print("下载完成")
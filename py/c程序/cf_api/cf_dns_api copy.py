#!/usr/bin/python
# -*- coding: UTF-8 -*-

import requests

import json

import pyperclip

# zone id
zid1 = ""

# api id
aut1 = ""
#可以在 cf网站的 My Profile -> API Tokens -> API Tokens -> Create Token 创建相应权限的 TOKEN，
# 这里只需要有相应 DNS 的编辑权限

# 网址
wz1 = ""

# ip
ip1 = "8.8.8.8"

#-----------------



#---------------

def dnslist_info(zid,aut,wz):

    # dns 网址 信息,查找 域名 的 id

    url = "https://api.cloudflare.com/client/v4/zones/" + zid + "/dns_records"

    headers = {
        "Content-Type": "application/json",
        "Authorization": aut
    }

    response = requests.request("GET", url, headers=headers)


    # 获取 回应 json dict类型
    zd = response.json()


    # 显示 dic 数据类型
    #print(type(dic),dic)

    #js = dic

    # json格式化 输出
    js = json.dumps(zd, sort_keys=True, indent=4, separators=(',', ':'))

    # print(js)

    #复制 文本 到剪贴板
    # pyperclip.copy(js)

    # 循环 查找 域名 的id
    for index in range(len(zd["result"])):

        # 判断 域名 的 名字
        if zd["result"][index]['name']  == wz :

            # 获取 域名 id
            wid1 = zd["result"][index]['id']
            break             
    
    return wid1


def dnsgx_ip(zid,id,wz,ip,aut):

    #更新 网址 dns 的ip

    url = "https://api.cloudflare.com/client/v4/zones/"+ zid + "/dns_records/" + id

    payload = {
        "content": ip,
        "name": wz,
        "proxied": True,
        "type": "A",
        "comment": "Domain verification record",
        "tags": [],
        "ttl": 1
    }
    headers = {
        "Content-Type": "application/json",
        "Authorization": aut
    }

    response = requests.request("PUT", url, json=payload, headers=headers)

    # 获取 回应 json dict类型
    rjg = response.json()

    #显示 结果 

    umsg = rjg["success"]
    # print(type(rjg),umsg)
    return umsg

domid = dnslist_info(zid1,aut1,wz1)
# dns 网址信息
print(wz1,"_dns id:",domid)

# dns 更新 ip

upip = dnsgx_ip(zid1,domid,wz1,ip1,aut1)

if upip == True :
    print(wz1,"ip 更新ok")
else :
    print(wz1,"ip 更新error")




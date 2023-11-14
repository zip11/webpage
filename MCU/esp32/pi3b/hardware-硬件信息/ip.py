#!/usr/bin/python
# -*- coding: UTF-8 -*-

import psutil

def GetLocalIPByPrefix(prefix):
    
    r"""
    多网卡情况下，根据前缀获取IP
    测试可用：Windows、Linux，Python 3.6.x，psutil 5.4.x
    ipv4/ipv6 地址均适用
    注意如果有多个相同前缀的 ip，只随机返回一个
    """
    localIP = ''
    dic = psutil.net_if_addrs()

    for adapter in dic:
    
        snicList = dic[adapter]
    
        for snic in snicList:
    
            if not snic.family.name.startswith('AF_INET'):
                continue                
    
            ip = snic.address
    
            if ip.startswith(prefix):
                localIP = ip
     
    return localIP     
     
print(GetLocalIPByPrefix('192.168'))
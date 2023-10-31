#!/usr/bin/python
# -*- coding: UTF-8 -*-

import socket
def GetLocalIPByPrefix(prefix):
    r""" 多网卡情况下，根据前缀获取IP（Windows 下适用） """
    localIP = ''
    for ip in socket.gethostbyname_ex(socket.gethostname())[2]:
        if ip.startswith(prefix):
            localIP = ip
    
    return localIP
    
print(GetLocalIPByPrefix('192.168'))
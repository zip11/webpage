import socket
import fcntl
import struct
import psutil
import time
import datetime

BOOT_TIME = psutil.boot_time()

def cpuper():

    cpup = psutil.cpu_percent(0)
    cpup = f'CPU USE:{cpup} %'
    
    return cpup


def cputemp():
    
    tempc = psutil.sensors_temperatures()
    tempc = tempc['cpu_thermal'][0][1]
    tempc = str(tempc)
    return tempc

def hum_convert(value):

    units = ["KB", "MB", "GB", "TB", "PB"]
    size = 1024.0
    for i in range(len(units)):
        if (value / size) < 1:
            return "%.0f%s" % (value, units[i])
        value = value / size

def getNet():
    
    # speed,upload,download 

    sent_before = psutil.net_io_counters().bytes_sent  # 已发送的流量
    recv_before = psutil.net_io_counters().bytes_recv  # 已接收的流量
    
    time.sleep(1)
    
    sent_now = psutil.net_io_counters().bytes_sent
    recv_now = psutil.net_io_counters().bytes_recv
    
    sent = (sent_now - sent_before)/1024  # 算出1秒后的差值
    recv = (recv_now - recv_before)/1024
    
    # tt1 = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

    tt1 = time.strftime("%m-%d %H:%M:%S", time.localtime())
    # print(tt1)
    

    sent1 = hum_convert(sent)
    up = f"UP:{sent1} "

    recv1 = hum_convert(recv)
    dn = f"DN:{recv1}   "


    spt = up + dn

    print(tt1+' '+spt, end="\r")

    return tt1,spt

def get_ip_address(prefix):

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

def get_up_time():

    up = time.time() - BOOT_TIME
    return datetime.datetime.fromtimestamp(up).strftime('%d-%H%M%S')

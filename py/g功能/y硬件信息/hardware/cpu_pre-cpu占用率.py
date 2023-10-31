# coding:utf-8
import psutil
import time

def getNet():
    
    sent_before = psutil.net_io_counters().bytes_sent  # 已发送的流量
    recv_before = psutil.net_io_counters().bytes_recv  # 已接收的流量
    
    time.sleep(1)
    
    sent_now = psutil.net_io_counters().bytes_sent
    recv_now = psutil.net_io_counters().bytes_recv
    
    sent = (sent_now - sent_before)/1024  # 算出1秒后的差值
    recv = (recv_now - recv_before)/1024
    
    tt1 = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    print(tt1)
    
    up = "UP:{0}KB/s ".format("%.0f"%sent)
    dn = "DN:{0}KB/s".format("%.0f"%recv)
    spt = up + dn

    print(spt)

    return tt1,spt
        
def cputemp():
    
    tempc = psutil.sensors_temperatures()
    tempc = tempc['cpu_thermal'][0][1]
    tempc = str(tempc)
    return tempc


def cpuper():

    cpup = psutil.cpu_percent(0)
    cpup = f'cpu use:{cpup} %'
    
    return cpup

if __name__ == "__main__":
    

    
    while 1:
        getNet()

        print(cpuper())

'''
深圳市普中科技有限公司（PRECHIN 普中）
技术支持：www.prechin.net
PRECHIN
 普中

实验名称：RTC实时时钟实验
接线说明：
         
实验现象：程序下载成功后，软件shell控制台间隔1S输出RTC实时时钟年月日时分秒星期
         
注意事项：

'''

#导入Pin模块
from machine import Pin
from machine import RTC
import time

# wifi 
import network
import ntptime



#路由器WIFI账号和密码
ssid="xzkt"
password="2018pryy"

#WIFI连接
def wifi_connect():
    
    wlan=network.WLAN(network.STA_IF)  #STA模式
    wlan.active(True)  #激活
    start_time=time.time()  #记录时间做超时判断
    
    if not wlan.isconnected():
        print("conneting to network...")
        wlan.connect(ssid,password)  #输入 WIFI 账号密码
        
        while not wlan.isconnected():
            print("wait wifi conneting")
            time.sleep_ms(300)
            print("wait wifi conneting")
            time.sleep_ms(300)
            
            #超时判断,15 秒没连接成功判定为超时
            if time.time()-start_time>15:
                print("WIFI Connect Timeout!")
                break
    
    else:
        
        print("network information:", wlan.ifconfig())


#定义RTC控制对象
rtc=RTC() 

#定义星期
week=("星期一","星期二","星期三","星期四","星期五","星期六","星期天")

#程序入口
if __name__=="__main__":
    
    wifi_connect()
    
    try:
        ntptime.NTP_DELTA = 3155644800 # 可选 UTC+8偏移时间（秒），不设置就是UTC0
        ntptime.host = 'ntp.aliyun.com' # 可选，ntp服务器，默认是"pool.ntp.org"
        ntptime.settime()
        
    except OSError :
        print("ntp链接超时,请重启!")
#     
#     if rtc.datetime()[0]!=2022:
#         rtc.datetime((2022,8,10,2,10,20,58,0))
    
    while True:
        date_time=rtc.datetime()
        print("%d-%d-%d \t %02d:%02d:%02d \t %s" %(date_time[0],date_time[1],date_time[2],
                                                   date_time[4],date_time[5],date_time[6],
                                                   week[date_time[3]]))
        time.sleep(1)

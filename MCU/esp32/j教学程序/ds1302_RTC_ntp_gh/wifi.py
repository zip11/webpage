# wifi 
import network
import time
# ntp
import ntptime
# rtc
import machine

# 1.连接wifi
# 2.ntp服务器-设置时间
# 3.读取 esp rtc 时间 元组


#路由器WIFI账号和密码
ssid="
password="

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


def set_time():

    # ntp网络设置时间
    try:
        ntptime.NTP_DELTA = 3155644800 # 可选 UTC+8偏移时间（秒），不设置就是UTC0
        ntptime.host = 'ntp.aliyun.com' # 可选，ntp服务器，默认是"pool.ntp.org"
        ntptime.settime()
        
    except OSError :
        print("ntp链接超时,请重启!")

def dis_rtc():
        
    # 显示 esp集成 rtc 时间
    #  
    #定义RTC控制对象
    rtc = machine.RTC()

    #定义星期
    week=("星期一","星期二","星期三","星期四","星期五","星期六","星期天")

    date_time=rtc.datetime()
    print("%d-%d-%d \t %02d:%02d:%02d \t %s" %(date_time[0],date_time[1],date_time[2],
                                                date_time[4],date_time[5],date_time[6],
                                                week[date_time[3]]))
    
    # 返回 元组
    date_time2=rtc.datetime()
    return date_time2
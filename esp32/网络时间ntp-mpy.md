# micropython实现ntp获取网络时间（UTC+8） #

[https://mpython.readthedocs.io/zh/master/library/micropython/ntptime.html#ntptime.settime](https://mpython.readthedocs.io/zh/master/library/micropython/ntptime.html#ntptime.settime)

    import ntptime

    def sync_ntp():
	     ntptime.NTP_DELTA = 3155644800   # 可选 UTC+8偏移时间（秒），不设置就是UTC0
	     ntptime.host = 'ntp1.aliyun.com'  # 可选，ntp服务器，默认是"pool.ntp.org"
	     ntptime.settime()   # 修改设备时间,到这就已经设置好了
    
    sync_ntp()
    
	# 已经设置好了，随便用
    from machine import RTC
    rtc = RTC()
    print(rtc.datetime())


NTP_DELTA常量的存在就让我们有了可乘之机，不改动代码的前提下，直接修改常量减掉8*3600秒就OK了。
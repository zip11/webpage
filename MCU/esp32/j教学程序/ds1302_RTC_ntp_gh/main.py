'''
深圳市普中科技有限公司（PRECHIN 普中）
技术支持：www.prechin.net
PRECHIN
 普中

实验名称：DS1302实时时钟实验
接线说明：DS1302时钟模块-->ESP32 IO
         (CE)-->(23)
         (IO)-->(19)
         (CK)-->(18)
         
实验现象：程序下载成功后，软件shell控制台间隔1S输出DS1302实时时钟年月日时分秒星期
         
注意事项：

'''

#导入Pin模块
from machine import Pin
import time
import DS1302

#定义DS1302控制对象
ds1302=DS1302.DS1302(clk=Pin(18),dio=Pin(19),cs=Pin(23))

#定义星期
week=("星期一","星期二","星期三","星期四","星期五","星期六","星期天")

#程序入口
if __name__=="__main__":
    if ds1302.DateTime()[0]!=2022:
        ds1302.DateTime([2022,8,10,2,11,3,58])
    while True:
        date_time=ds1302.DateTime()
        print("%d-%d-%d \t %02d:%02d:%02d \t %s" %(date_time[0],date_time[1],date_time[2],
                                                   date_time[4],date_time[5],date_time[6],
                                                   week[date_time[3]]))
        time.sleep(1)
        
'''
深圳市普中科技有限公司（PRECHIN 普中）
技术支持：www.prechin.net
PRECHIN
 普中
 
实验名称：定时器中断实验
接线说明：LED模块-->ESP32 IO
         (D1)-->(15)
         
实验现象：程序下载成功后，D1指示灯间隔0.5s状态翻转
注意事项：

'''

#导入Pin模块
from machine import Pin
from machine import Timer
import time

#定义LED控制对象
led1=Pin(15,Pin.OUT)


#定义LED状态
led1_state=0

sectot1=11



#定时器0中断函数
def time0_irq(time0):
    
    global sectot1
    
    sectot1 = sectot1-1

        
#程序入口
if __name__=="__main__":
 
    
    time0=Timer(0)  #创建time0定时器对象
    time0.init(period=1000,mode=Timer.PERIODIC,callback=time0_irq)
    
    while True:
        print(str(sectot1))
        time.sleep(1)

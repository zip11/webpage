'''
深圳市普中科技有限公司（PRECHIN 普中）
技术支持：www.prechin.net
PRECHIN
 普中

实验名称：PWM呼吸灯实验
接线说明：LED模块-->ESP32 IO
         (D1)-->(15)
         
实验现象：程序下载成功后，D1指示灯呈现呼吸灯效果，由暗变亮，再由亮变暗
注意事项：

'''

#导入Pin模块
from machine import Pin
from machine import PWM
import time

#定义LED1控制对象
led1=PWM(Pin(15),freq=1000,duty=0)

def beep_max_min():
    
    # pwm占空比 先变大，再变小
    
    duty_value=0
    fx=1
    while True:
        
        # pwm占空比 先变大
        if fx==1:
            duty_value+=10
            if duty_value>523:
                fx=0
        else:
            duty_value-=10
            if duty_value<10:
                fx=1
        
        time.sleep_ms(10)
        led1.duty(duty_value)

#程序入口
if __name__=="__main__":

        # 固定占空比
        led1.duty(777)
        
        # 占空比 先打，再小
#         beep_max_min()
        
        

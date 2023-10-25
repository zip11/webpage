'''
深圳市普中科技有限公司（PRECHIN 普中）
技术支持：www.prechin.net
PRECHIN
 普中

实验名称：数码管显示实验
接线说明：数码管模块-->ESP32 IO
         CLK-->(16)
         DIO-->(17)
         
实验现象：程序下载成功后，数码管间隔1s从0开始计数显示
         
注意事项：

'''

#导入Pin模块
from machine import Pin
import time
import tm1637


#定义按键控制对象
key1=Pin(14,Pin.IN,Pin.PULL_UP)
key2=Pin(27,Pin.IN,Pin.PULL_UP)
key3=Pin(26,Pin.IN,Pin.PULL_UP)
key4=Pin(25,Pin.IN,Pin.PULL_UP)


#定义LED状态
led1_state,led2_state,led3_state,led4_state=0,0,0,0

ccs=0

#KEY1外部中断函数
def key1_irq(key1):
    global led1_state
    global ccs
    time.sleep_ms(10)
    if key1.value()==0:
        ccs=ccs+1
        
        led1_state=not led1_state
        print(led1_state)

#KEY2外部中断函数
def key2_irq(key2):
    global led2_state
    time.sleep_ms(10)
    if key2.value()==0:
        led2_state=not led2_state




##----------------


#定义数码管控制对象
smg=tm1637.TM1637(clk=Pin(16),dio=Pin(17))

def minsec(sec2):
    #01:33,

    min1 = "0"
    sec1 = "0"
    
    min1 = min1 + str(sec2//60)
   
    sec1 = sec1 + str(sec2%60)
    
    min1 = min1[-2:]
    sec1 = sec1[-2:]
    
    print("min:"+min1)
    print("sec:"+sec1)
    
    wb1 = min1 + sec1
    
    return wb1
    
    
    
def flash():
    
    # smg flash
    smg.show("    ")
    time.sleep(1)
    smg.show("oooo")
    

#程序入口
if __name__=="__main__":
    #smg.numbers(1,24)  #显示小数01.24
    #smg.hex(123)  #将十进制数转换十六进制显示
    #smg.brightness(0)  #亮度调节
    #smg.temperature(25)  #显示带温度符号°C，整数温度值
    #smg.show("1314")  #字符串显示，显示整数
    #smg.scroll("1314-520",500)  #字符串滚动显示，速度调节
    #time.sleep(5)
    
    key1.irq(key1_irq,Pin.IRQ_FALLING)  #配置key1外部中断，下降沿触发
    
    n = 5*60+12
    
    while True:
        
        # smg display
        #smg.number(n)
        smg.show(minsec(n))
        
        # scan key            
    
        # run clock
        if(n>0 and led1_state):
            # -1ms 
            n-=1
        elif(n==0):
            # clock end,  flash smg
            flash()

            
        
        # delay 1s
        time.sleep(1)
        print("total_sec:",n)

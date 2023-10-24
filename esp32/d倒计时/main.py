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



#定义按键键值
KEY1_PRESS,KEY2_PRESS,KEY3_PRESS,KEY4_PRESS=1,2,3,4
key_en=1
#按键扫描函数
def key_scan():
    global key_en  #全局变量
    if key_en==1 and (key1.value()==0 or key2.value()==0 or
                      key3.value()==0 or key4.value()==0 ):
        time.sleep_ms(10)  #消斗
        key_en=0
        if key1.value()==0:
            return KEY1_PRESS
        elif key2.value()==0:
            return KEY2_PRESS
        elif key3.value()==0:
            return KEY3_PRESS
        elif key4.value()==0:
            return KEY4_PRESS
    elif key1.value()==1 and key2.value()==1 and key3.value()==1 and key4.value()==1:
        key_en=1
    return 0

def key_fact():
        key=key_scan()  #按键扫描
        print("key:",key)
        
        if key==KEY1_PRESS:  #K1键按下
            return "on"
        elif key==KEY2_PRESS:  #K2键按下
            return "k2"
        elif key==KEY3_PRESS:  #K3键按下
            pass
        elif key==KEY4_PRESS:  #K4键按下
            pass 

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
    
    n = 5*60+12
    
    stat = "off"
    stat2 = "off"
    
    end2 = "off"
    
    while True:
        
        # smg display
        #smg.number(n)
        smg.show(minsec(n))
        
        # scan key
        stat = key_fact()
        
        if(stat == "on" or end2 == "on"):
            stat2 = "on"
            end2 = "on"
        elif(stat == "k2"):
            n = 12
    
            
            
        
        # run clock
        if(n>0 and stat2 == "on"):
            # -1ms 
            n-=1
        elif(n==0):
            # clock end,  flash smg
            flash()
            end2 = "off"
            stat == "off"
            stat2 == "off"
            
        
        # delay 1s
        time.sleep(1)
        print("total_sec:",n)

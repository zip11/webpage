# read api
import urequests
import ujson

# wifi
import network
import time

#导入Pin模块
from machine import Pin
import time
from machine import SoftI2C
from ssd1306 import SSD1306_I2C  #I2C的oled选该方法

# 和风天气的账号，并且获得一个API Key

api_key = ""


#路由器WIFI账号和密码
ssid=""
password=""

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






# city_name = input("请输入城市名称：")
city_name = "wuhan"

    
# 通过城市查询接口获取城市ID

def city_id(apikey,city_name,language='en',unit='c'):
    
#   language='zh-Hans'  en
    url_now=f'https://api.seniverse.com/v3/location/search.json?key={apikey}&q={city_name}&language={language}'
    
    nowResult = urequests.get(url_now)
    
    json=ujson.loads(nowResult.text)
    nowResult.close()
    
    ctid_str = json["results"][0]["id"]
    
    return ctid_str

# 实时天气
def city_now(apikey,,language='en'):
    
#     city_id='ip'使用ip定位
    url_now=f'https://api.seniverse.com/v3/weather/now.json?key={apikey}&location={city_id}&language={language}'
    
    nowResult = urequests.get(url_now)
    
    json=ujson.loads(nowResult.text)
    nowResult.close()
    
    #json 解析
    j_now = json["results"][0]
    
    
    return j_now


#创建硬件I2C对象
#i2c=I2C(0,sda=Pin(19), scl=Pin(18), freq=400000)

#创建软件I2C对象
i2c = SoftI2C(sda=Pin(23), scl=Pin(18))
#创建OLED对象，OLED分辨率、I2C接口
oled = SSD1306_I2C(128, 64, i2c) 

    
if __name__=="__main__":
    
    
    
    wifi_connect()
    
    # city id string，输入城市名字，获取城市id
#     ctid = city_id(api_key,"wuhan")
    
#     print(f'city_id:{ctid}')
    
    #实时天气
#     jnr = city_now(api_key,ctid)


#  ip获取 实时天气··············
    jnr = city_now(api_key,)
    print(jnr)

    wd1 = jnr['now']["temperature"]
    print(wd1)

    tq1 = jnr["now"]["text"]
    print(tq1)
    
    loc1 = jnr['location']['name']
    print(f"location: {loc1}")

    #oled location: -------------
    oled.fill(0)  #清空屏幕
    oled.show()  #执行显示

    oled.text(f"location: {loc1}",0,0,1)

    oled.text(f"weather: {tq1} ",0,20,1)
    #显示 weather
    
    oled.text(f"temp: {wd1}C ",0,40,1)
    #显示temp
        
    oled.show()
    #执行显示  
    
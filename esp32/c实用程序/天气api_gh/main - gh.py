# read api
import urequests
import ujson

# wifi
import network
import time

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
    
    def city_id(apikey,city_name,language='zh-Hans',unit='c'):
        
        url_now=f'https://api.seniverse.com/v3/location/search.json?key={apikey}&q={city_name}'
        
        nowResult = urequests.get(url_now)
        
        json=ujson.loads(nowResult.text)
        nowResult.close()
        
        ctid_str = json["results"][0]["id"]
        
        return ctid_str
    
    # 实时天气
    def city_now(apikey,city_id):
        
        url_now=f'https://api.seniverse.com/v3/weather/now.json?key={apikey}&location={city_id}'
        
        nowResult = urequests.get(url_now)
        
        json=ujson.loads(nowResult.text)
        nowResult.close()
        
        #json 解析
        j_now = json["results"][0]
        
        
        return j_now
    
if __name__=="__main__":
    

    
    wifi_connect()
    
    # city id string
    ctid = city_id(api_key,"wuhan")
    print(f'city_id:{ctid}')
    
    #实时天气
    jnr = city_now(api_key,ctid)

    wd1 = jnr['now']["temperature"]
    print(wd1)

    tq1 = jnr["now"]["text"]
    print(tq1)

    
    
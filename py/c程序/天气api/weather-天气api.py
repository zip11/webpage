import requests
import time
import os

# 和风天气的账号，并且获得一个API Key

api_key = ""
# city_name = input("请输入城市名称：")
city_name = "beijing"

# 通过城市查询接口获取城市ID
city_url = f"https://geoapi.qweather.com/v2/city/lookup?key={api_key}&location={city_name}&lang=zh"

city_response = requests.get(city_url)
city_data = city_response.json()

if city_data["code"] == "200":

    city_id = city_data["location"][0]["id"]
    print(f"城市 {city_name} 对应的城市ID 为：{city_id}")
    
    # 使用城市ID查询实时天气信息
    weather_url = f"https://devapi.qweather.com/v7/weather/now?key={api_key}&location={city_id}"
    weather_response = requests.get(weather_url)
    weather_data = weather_response.json()

    if weather_data["code"] == "200":

        now = weather_data["now"]
        print(f"{city_name}的天气情况：")
        print(f"天气状况：{now['text']}")
        print(f"温度：{now['temp']}℃")
        print(f"体感温度：{now['feelsLike']}℃")
        print(f"风向：{now['windDir']}")
        print(f"风速：{now['windSpeed']}km/h")

    else:
        print("获取天气信息失败！")
else:
    print("获取城市信息失败！")

time.sleep(5)


os.system("pause")

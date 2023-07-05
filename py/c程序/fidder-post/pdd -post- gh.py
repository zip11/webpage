import requests
import json

# post 发送 json ，设置代理 通过fidler

# pdd

headers2 = {
    "Content-Type": "application/json; charset=UTF-8",
    "Referer": "dd",
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Safari/537.36",
    }

url = "https://jinbao.pinduoduo.com/network/api/common/goodsList"

pyload = {"keyword": "", "sortType": 0, "withCoupon": 0, "categoryId": 16, "pageNumber": 1, "pageSize": 60}


# pdd
# response = requests.post(url, data=json.dumps(pyload), headers=headers,proxies={'https':'https://127.0.0.1:8888'}).text

# jd

# dl1={'https':'http://127.0.0.1:8888'}
dl1={'https':'127.0.0.1:8888'}

jdata = json.dumps(pyload)
# jdata = pyload2

# 
s = requests.session()

# 设置连接活跃状态为False
s.keep_alive = False

response = requests.post(url, data= jdata,headers = headers2,proxies=dl1,verify=False)
# verify=False ssl证书禁止校验

print(response.text)

# 关闭请求  释放内存
response.close()
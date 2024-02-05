import requests

import json

# 1. 打开并加载JSON文件
with open('data.json', 'r') as file:
    data = json.load(file)

# 读取 json，选项
token1 = data["token2"]
# token1 = ""

url = "https://oapi.dingtalk.com/robot/send?access_token=" + token1

headers = {
    "Content-Type": "application/json"
}
data = {
    "msgtype": "text",
    "text": {
        "content": "监控，我就是我, 是不一样的烟火"
    }
}

# post，发送消息
response = requests.post(url, headers=headers, json=data)

# 如果需要检查响应状态码或获取响应内容
if response.status_code == 200:
    # print("消息发送至服务器",response.text)
    
    #json转 py字典
    response_json = json.loads(response.text)

    # 检查 response.text返回json，是否errcode==0
    if response_json["errcode"] != 0:
        print("消息内容有错误:",response.text)
    else:
        print("消息发送成功",response.text)

else:
    print(f"消息发送失败，错误代码：{response.status_code}")
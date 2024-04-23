import requests
import json


def post_request(url, id,api_key):

    url = url + "/api/member/base"

    # 请求头部
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
        "x-api-key": api_key
    }
    
    # 请求参数
    data = {
        'id': id
    }
    
    # 发送 POST 请求
    response = requests.post(url, headers=headers, data=data)
    
    # print(response.text)

    # 解析 JSON 响应
    json_data = response.json()
    
    # """

    # 显示人类可视化的 JSON 数据
    print("请求结果：")
    print("消息：", json_data.get("message"))
    print("数据：", json_data.get("data"))
    print("代码：", json_data.get("code"))

    # """

# 从 key.json 文件读取 API 密钥
def get_api_key(number):

    key_path = "key.json"
    key_path2 = "key_true.json"

    # 切换 api key 文件
    if number == 1:
        key_file = key_path
        print("test website","key.json")
    elif number == 2:
        key_file = key_path2
        print("true website","key_true.json")



    try:
        with open(key_file, "r") as f:
            data = json.load(f)
            api_key = data.get("api_key")
            return api_key
    except Exception as e:
        print("读取 API 密钥出错:", e)
        return None
    

# 调用函数并传递网址和id
    
# 测试网站 
url = "https://test2.m-team.cc"

id = 246176

# 获取 API 密钥   1，test 2，true
api_key = get_api_key(1)

post_request(url, id,api_key)

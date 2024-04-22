import requests
import json

# 测试网站 
# base_url = "https://test2.m-team.cc"
# 实际 网站
base_url = "https://kp.m-team.cc"

def search_torrents(api_key, url):

    headers = {
        "x-api-key": api_key,
        "Content-Type": "application/json"
    }
    payload = {
        "mode": "adult",
        "categories": [],
        "onlyFav": 1,
        "visible": 1,
        "pageNumber": 1,
        "pageSize": 100
    }

    try:

        response = requests.post(url, headers=headers, json=payload)

        if response.status_code == 200:

            # HTTP 响应的 JSON 数据解析为 Python 字典
            data = response.json()

            # 输出人类可读的JSON响应
            print(json.dumps(data, indent=4, ensure_ascii=False))

            return data
        else:
            print("请求失败，状态码:", response.status_code)
    except Exception as e:
        print("请求出错:", e)

# 从 key.json 文件读取 API 密钥
def get_api_key():
    try:
        with open("key.json", "r") as f:
            data = json.load(f)
            api_key = data.get("api_key")
            return api_key
    except Exception as e:
        print("读取 API 密钥出错:", e)
        return None


# mian
if __name__ == "__main__":

    # 在这里替换成你的API网址
    api_url = base_url + "/api/torrent/search"

    # 获取 API 密钥
    api_key = get_api_key()

    if api_key:

        data = search_torrents(api_key, api_url)

        # 提取id信息,     id  |  data->data
        id_list = [item['id'] for item in data['data']['data']]
        print("提取到的id信息:", id_list)

        name_list = [item['name'] for item in data['data']['data']]
        print("提取到的name信息:", name_list)
        


    else:
        print("API 密钥未提供，请检查 key.json 文件。")

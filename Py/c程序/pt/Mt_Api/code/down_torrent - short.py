import requests
import json

def get_download_link(item_id, api_key):

    # 设置网址和命令路径
    base_url = "https://test2.m-team.cc"
    api_path = "/api/torrent/genDlToken"

    # 设置请求头
    headers = {
        "x-api-key": api_key
    }

    # 构造参数
    params = {
        "id": item_id
    }

    # 发送POST请求
    response = requests.post(f"{base_url}{api_path}", headers=headers, data=params)

    # 检查响应状态码
    if response.status_code == 200:
        # 解析JSON响应
        data = response.json()
        download_link = data.get("data")
        if download_link:
            return download_link
        else:
            return None
    else:
        print("请求失败，状态码:", response.status_code)
        return None
    
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

def main():

    # 获取用户输入的数字变量和API密钥
    item_id = input("请输入数字变量: ")

    # 获取 API 密钥
    api_key = get_api_key()
    # api_key = input("请输入API密钥: ")

    # 获取下载链接
    download_link = get_download_link(item_id, api_key)

    if download_link:
        print("下载链接:", download_link)
    else:
        print("未找到下载链接")

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

if __name__ == "__main__":
    main()

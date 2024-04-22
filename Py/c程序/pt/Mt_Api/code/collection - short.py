import requests
import json

# 修改收藏夹中的种子 ,收藏 ，取消收藏

# 测试网站 
base_url = "https://test2.m-team.cc"

def modify_collection(torrent_id, api_key, add_to_collection=True):

    url = base_url + "/api/torrent/collection"
    headers = {
        "x-api-key": api_key,
        "Content-Type": "application/x-www-form-urlencoded"
    }
    data = {
        "id": torrent_id,
        "make": str(add_to_collection).lower()
    }
    response = requests.post(url, headers=headers, data=data)
    print(response.text)

    json_response = response.json()  # 解析JSON响应

    if json_response.get("message") == "SUCCESS":
        return True
    else:
        return False


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

# 使用示例
torrent_id = 766754
api_key = get_api_key()

# 添加到收藏夹
# response_add = modify_collection(torrent_id, api_key)
# print("添加到收藏夹的响应:", response_add)

# 从收藏夹中移除

response_remove = modify_collection(torrent_id, api_key, add_to_collection=False)
# print("从收藏夹中移除的响应:", response_remove)

if response_remove :
    print("成功从收藏夹中移除!")
else:
    print("从收藏夹中移除失败.")

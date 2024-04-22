import requests
import json
import time

# 修改收藏夹中的种子 ,收藏 ，取消收藏

# 测试网站 
# base_url = "https://test2.m-team.cc"
# 实际 网站
base_url = "https://kp.m-team.cc"

# 函数，修改收藏夹中的种子
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

    # 发送POST请求
    response = requests.post(url, headers=headers, data=data)
    print(response.text)

    # 解析JSON响应
    json_response = response.json()  
    
    # 检查响应是否成功
    if json_response.get("message") == "SUCCESS":
        return True
    else:
        return False

# 函数，批量取消收藏
def remove_from_collection(api_key, torrent_ids):

    for torrent_id in torrent_ids:
        # 移除收藏夹中的种子 单个
        response_remove = modify_collection(torrent_id, api_key, add_to_collection=False)
        
        if response_remove :
            print(f"{torrent_id}成功从收藏夹中移除!")
        else:
            print(f"{torrent_id} 从收藏夹中移除失败!.")
        time.sleep(2)  
        # 避免过快请求
    
def search_torrents(api_key, url,fenlei2,pagesize):

    # 获取 收藏 种子

    # 设置请求头

    headers = {
        "x-api-key": api_key,
        "Content-Type": "application/json"
    }

    # 收藏 分类
    fenlei = ["adult","movie"]

    # 构造请求参数
    payload = {
        "mode": fenlei[fenlei2],
        "categories": [],
        "onlyFav": 1,
        "visible": 1,
        "pageNumber": 1,
        "pageSize": pagesize
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

    # key_file = "key.json"
    key_file = "key_true.json"

    try:
        with open(key_file, "r") as f:
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

# response_remove = modify_collection(torrent_id, api_key, add_to_collection=False)
# print("从收藏夹中移除的响应:", response_remove)



# main 函数
if __name__ == "__main__":

    # API网址
    api_url = base_url + "/api/torrent/search"

    if api_key:

        # 搜索种子  ,0 ad 1 movie ,11 单页种子 数量
        data = search_torrents(api_key, api_url,0,11)


        # 提取id信息,     id  |  data->data
        id_list = [item['id'] for item in data['data']['data']]
        print("提取到的id信息:", id_list)

        # 批量取消收藏
        remove_from_collection(api_key, id_list)


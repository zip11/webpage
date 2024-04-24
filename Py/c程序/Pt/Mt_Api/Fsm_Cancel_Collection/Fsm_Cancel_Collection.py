import requests
import json
import collection

# 

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
            # print(json.dumps(data, indent=4, ensure_ascii=False))

            return data
        else:
            print("请求失败，状态码:", response.status_code)
    except Exception as e:
        print("请求出错:", e)

# 从 key.json 文件读取 API 密钥
def get_api_key():
    try:
        with open("key_true.json", "r") as f:
            data = json.load(f)
            api_key = data.get("api_key")
            return api_key
    except Exception as e:
        print("读取 API 密钥出错:", e)
        return None

# 取消收藏
def cancel_collection(api_key,name_list,id_list,remove_torrent ):
        
    # 转大写字母
    remove_torrent = remove_torrent.upper()

    # name_list 查找是否有包含 remove_torrent 的name,如果有则取消收藏


    for name in name_list:

        print(name)
        # 查找 是否有包含 remove_torrent 的name,如果有则取消收藏
        if remove_torrent in name.upper():

            # 提取id信息,     id  |  data->data
            index = name_list.index(name)
            
            # 取消收藏
            torrent_id = id_list[index]

            collection.modify_collection(torrent_id, api_key, add_to_collection=False)
            print(f"取消收藏: {remove_torrent} ~~~~~~~~~~~~~~~~~~~~~")
            
            break
            
        else:
            print(f"未找到: {remove_torrent}")

# 函数，读取json文件内 文件名字符串 
def read_json_file(file_path):

    with open(file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)
        return data


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
        # print("提取到的id信息:", id_list)

        name_list = [item['name'] for item in data['data']['data']]
        print("提取到的name信息:", name_list)

        # 读取json，文件内 文件名字符串
        cancel_tor = read_json_file("file_parts.json")
        
        # 遍历cancel_tor 内的 文件名字符串
        for tor in cancel_tor:

            # 取消收藏
            cancel_collection(api_key,name_list,id_list,tor)

        


    else:
        print("API 密钥未提供，请检查 key.json 文件。")


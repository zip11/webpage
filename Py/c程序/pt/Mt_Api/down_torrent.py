import requests
import json
import time
import re

# mt Api 批量下载 收藏的 种子

# 测试网站 
# base_url = "https://test2.m-team.cc"
# 实际 网站
base_url = "https://kp.m-team.cc"

def get_download_link(item_id, api_key):

    # 获取 单个帖子的 下载链接

    # 设置网址和命令路径

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
    



def download_files(download_urls, file_names,api_key):

    # 下载 单个 种子

    # 确保下载链接和文件名列表长度相同
    if len(download_urls) != len(file_names):
        print("下载链接和文件名数量不匹配")
        return
    
    # 遍历下载链接和文件名
    for url, name in zip(download_urls, file_names):

        # http请求头：x-api-key
        headers = {
            "x-api-key": api_key
        }

        # 发送GET请求并下载文件
        response = requests.get(url, headers=headers)

        if response.status_code == 200:
            # 保存文件
            with open(name, 'wb') as file:
                file.write(response.content)
            print(f"文件 {name} 下载成功")
            time.sleep(3)  # 延时1秒
        else:
            print(f"下载 {url} 失败")



    
def search_torrents(api_key, url):

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
        "mode": fenlei[1],
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



def download_files_all(id_list, name_list,api_key):

    # 下载 全部收藏 种子

    # 提取下载链接,每次延时3s
    download_urls = []

    for item_id in id_list:

        download_link = get_download_link(item_id, api_key)
        download_urls.append(download_link)
        print(f"正在获取 {item_id} 的下载链接...")
        # 延时3秒
        time.sleep(3)
        
    # 下载文件
    download_files(download_urls, name_list,api_key)
    
    print("所有文件下载完成。")

def clean_filename(filename):

    # 删除Windows非法字符
    cleaned_filename = re.sub(r'[\\/:*?"<>|]', '', filename)
    return cleaned_filename

def generate_torrent_names(name_list, extension='.torrent'):

    # 生成 种子文件名 ,添加扩展名
    torrent_names = []

    for name in name_list:
        cleaned_name = clean_filename(name)
        torrent_name = cleaned_name + extension
        torrent_names.append(torrent_name)
    return torrent_names

def main():

    # API网址
    api_url = base_url + "/api/torrent/search"

    # 获取 API 密钥
    api_key = get_api_key(2)

    if api_key:

        # 搜索种子
        data = search_torrents(api_key, api_url)

        # 提取id信息,     id  |  data->data
        id_list = [item['id'] for item in data['data']['data']]
        print("提取到的id信息:", id_list)

        # 提取name信息,     name  |  data->data->name
        name_list = [item['name']  for item in data['data']['data']]
        
        # 生成 种子文件名
        name_list = generate_torrent_names(name_list)
        print("提取到的name信息:", name_list)


        # 下载所有文件
        download_files_all(id_list, name_list,api_key)
        


    else:
        print("API 密钥未提供，请检查 key.json 文件。")






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

if __name__ == "__main__":
    main()

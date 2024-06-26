import requests
import json
import time
import re
import os
# 取消 收藏 种子
import collection

# mt Api 批量下载 收藏的 种子，下载完成后 取消收藏

# 测试网站 
# base_url = "https://test2.m-team.cc"
# 实际 网站
base_url = "https://kp.m-team.cc"

# 种子路径 ".\\Mt_Ad"


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

    # 获取当前文件夹路径
    current_dir = os.getcwd()

    folder_path = os.path.join(current_dir,"Mt_Ad")
    # 判断 文件夹 存在
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
        print("文件夹已创建")
    else:
        print("文件夹已存在")


    # 确保下载链接和文件名列表长度相同
    if len(download_urls) != len(file_names):
        print("下载链接和文件名数量不匹配")
        return
    
    # 遍历下载链接和文件名
    for url, name in zip(download_urls, file_names):

        # 发送GET请求并下载文件 
        response = requests.get(url)

        if response.status_code == 200:

            # torrent全路径
            name = os.path.join(folder_path,name)

            # 保存文件
            with open(name, 'wb') as file:
                file.write(response.content)
            print(f"文件 {name} 下载成功")
            time.sleep(2)  # 延时1秒
        else:
            print(f"下载 {url} 失败")



    
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



def download_files_all(id_list, name_list,api_key):

    # 下载 全部收藏 种子

    # 提取下载链接,每次延时3s
    download_urls = []

    for item_id in id_list:

        download_link = get_download_link(item_id, api_key)
        download_urls.append(download_link)
        print(f"正在获取 {item_id} 的下载链接...")
        # 延时3秒
        time.sleep(2)
        
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
    


def main():

    print("mt Api 批量下载 收藏的 种子，下载完成后 取消收藏")

    # API网址
    api_url = base_url + "/api/torrent/search"

    # 获取 API 密钥   1，test 2，true
    api_key = get_api_key(2)

    # API 密钥 验证
    if api_key:

        
        tor_number = 11
        tor_fenlei = 0

        print("下载文件分类,0 ad ,1 movie ")
        print(f"下载文件分类{tor_fenlei},单页种子 数量{tor_number}")

        # 搜索种子  ,0 ad 1 movie ,11 单页种子 数量
        data = search_torrents(api_key, api_url,tor_fenlei,tor_number)


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

        # 批量 删除 收藏 种子
        collection.remove_from_collection(api_key,id_list)
        


    else:
        print("API 密钥未提供，请检查 key.json 文件。")








if __name__ == "__main__":
    main()

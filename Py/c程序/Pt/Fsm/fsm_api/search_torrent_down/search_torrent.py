import requests
import json
import time

# 定义一个空列表来  存储没有找到匹配的种子
null_keyword = []

# 定义一个列表来  存储下载种子
down_keyword = []

# 搜索种子
def search_torrents(APITOKEN,keyword):

    # print(APITOKEN)

    try:

        # 定义 API 请求 URL
        url = f"https://api.fsm.name/Torrents/listTorrents?type=0&systematics=0&tags=[]&keyword={keyword}&page=1"

        # 发送 GET 请求获取网页内容
        headers = {'APITOKEN': APITOKEN}
        response = requests.get(url,headers=headers)


        # 如果请求成功，解析 JSON 数据
        if response.status_code == 200:

            # 应答 转 json
            data = response.json()

            # 检查是否存在搜索结果
            if 'success' in data and data['success'] and 'data' in data and 'list' in data['data']:

                torrents = data['data']['list']
                
                if torrents:
                    return torrents
                else:
                    print("未找到匹配的种子")
                    return []
            else:
                print("API 请求失败或返回的数据不正确")
                return []
            
        else:
            print(f"请求失败，状态码: {response.status_code}")
            return []
    except Exception as e:
        print(f"发生异常: {e}")
        return []
    



    
#  获取 下载帖子 tid
def torrent_id(torrents):

    # 输出搜索结果
    if torrents:

        print("搜索结果:")

        # 判断 torrents 元素数量 是否只有1个
        if len(torrents) == 1:

            torrent = torrents[0]

            # tid 存在
            if 'tid' in torrent and torrent['tid']:

                # json 可读化
                formatted_json = json.dumps(torrent, indent=4, ensure_ascii=False)

                # 显示 搜索 结果
                print(formatted_json )

                # 换行
                print("\n~~~~~~~~~~~~~~~~~~\n")

                # 获取 json内的 tid ，title
                tid = torrent['tid']
                title = torrent['title']

                return tid,title

    else:
        print(" 含有 多个 搜索 结果")
        return None,None



# 下载种子
def down_torrent_link(passkey,tid,local_filename):

    url = f"https://fsm.name/api/Torrents/download?tid={tid}&passkey={passkey}&source=direct"

    print("下载链接:",url)
    # 下载文件 dl_link

    # 发送HTTP请求
    response = requests.get(url, stream=True)
    response.raise_for_status()

    # 保存文件 名字
    local_filename = local_filename + ".torrent"

    # 将文件保存到本地
    with open(local_filename, 'wb') as f:
        for chunk in response.iter_content(chunk_size=8192):
            if chunk:  # 过滤掉keep-alive新块
                f.write(chunk)
                
    print(f"{local_filename} 文件下载完成")


def read_json(filename):

    # 读取JSON文件并加载内容
    with open(filename, 'r') as file:
        data = json.load(file)

    # 获取contentArray列表并返回
    content_array = data.get('contentArray', [])
    return content_array

# 保存 down_keyword 列表到 JSON 文件
def save_to_json(filename, data):

    # 将 data 转换为 JSON 字符串
    json_data = json.dumps(data, indent=4)

    # 将 JSON 字符串写入文件
    with open(filename, 'w') as file:
        file.write(json_data)

# 从 key.json 文件读取 API 密钥
def get_api_key():

    try:
        with open("key.json", "r") as f:
            
            # 读取 JSON 数据
            data = json.load(f)
            api_key = data.get("api_key")
            return api_key
    except Exception as e:
        print("读取 API 密钥出错:", e)
        return None
    
# passkey 密钥
def get_passkey_key():

    try:
        with open("key.json", "r") as f:
            
            # 读取 JSON 数据
            data = json.load(f)
            api_key = data.get("passkey")
            return api_key
    except Exception as e:
        print("读取 passkey 密钥出错:", e)
        return None


def main(keyword):

    
    # 读取 API 密钥
    APITOKEN =  get_api_key()

    # 读取 torrent 密钥
    PASSKEY = get_passkey_key()

    # 输入搜索关键字
    # keyword = input("请输入搜索关键字: ")

    # 调用函数搜索种子
    torrents = search_torrents(APITOKEN,keyword)
    time.sleep(1)


    #  获取 种子 tid
    tid, title = torrent_id(torrents)
    time.sleep(1)

    
    # 判断 tid 是否为 None
    if tid is not None:

        # 下载种子
        down_torrent_link(PASSKEY,tid,title)
        down_keyword.append(keyword)
        time.sleep(1)
        
    else:
        print(f"{keyword} torrents 变量为 None，请检查。")
        null_keyword.append(keyword)
    
    print(f"{down_keyword} 下载种子成功")
    # 保存 down_keyword 列表到 JSON 文件
    save_to_json("down_keyword.json", down_keyword)

    print(f"null keyword:",null_keyword)
    # 保存 null_keyword 列表到 JSON 文件
    save_to_json("null_keyword.json", null_keyword)

    print("end !!!")



if __name__ == "__main__":

    # JSON文件
    filename = 'content.json'
    
    # 读取JSON文件
    content_list = read_json(filename)

    print(content_list)

    # 遍历 content_list 列表
    for content in content_list:

        # 调用 main 函数
        main(content)

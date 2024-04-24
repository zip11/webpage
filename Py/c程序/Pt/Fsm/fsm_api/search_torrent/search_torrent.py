import requests
import json

# 搜索种子
def search_torrents(APITOKEN,keyword):

    print(APITOKEN)

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
    


def main():

    # 读取 API 密钥
    APITOKEN =  get_api_key()

    # 输入搜索关键字
    keyword = input("请输入搜索关键字: ")

    # 调用函数搜索种子
    torrents = search_torrents(APITOKEN,keyword)

    # 输出搜索结果
    if torrents:

        print("搜索结果:")

        for torrent in torrents:

            # tid 存在
            if 'tid' in torrent and torrent['tid']:

                # json 可读化
                formatted_json = json.dumps(torrent, indent=4, ensure_ascii=False)

                # 显示 搜索 结果
                print(formatted_json )

                # 换行
                print("\n~~~~~~~~~~~~~~~~~~\n")

    else:
        print("未找到任何种子")

if __name__ == "__main__":

    main()

import requests


# API 地址和密钥
URL = "https://api.fsm.name"

# 你的APITOKEN
APITOKEN = ""


# 读取 用户 passkey
def get_passkey(url):

    try:

        # 发送 GET 请求获取网页内容
        headers = {'APITOKEN': APITOKEN}
        response = requests.get(url,headers=headers)

        # 如果请求成功，解析 JSON 数据
        if response.status_code == 200:

            data = response.json()

            # 检查 JSON 中是否存在 passkey 字段
            if 'data' in data and 'passkey' in data['data']:
                passkey = data['data']['passkey']
                return passkey
            else:
                print("JSON 数据中缺少 passkey 字段")
                return None
        else:
            print(f"请求失败，状态码: {response.status_code}")
            return None
        
    except Exception as e:
        print(f"发生异常: {e}")
        return None

def main():

    # 定义网页的 URL
    url = f"{URL}/Users/infos"

    # 调用函数获取 passkey
    passkey = get_passkey(url)

    if passkey:
        print(f"提取到的 passkey 为: {passkey}")
    else:
        print("未能成功提取 passkey")

if __name__ == "__main__":

    main()

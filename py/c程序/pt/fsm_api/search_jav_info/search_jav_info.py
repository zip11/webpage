
import requests
import json

# 获取 jav 信息
def get_jav_info(torrent_name):

    res = requests.get(f"https://javdb.fsm.name/Movies/{torrent_name}").json()
    
    # 获取 返回值 结果
    if res.get('success'):

        # 原始 json 内容
        display_json(res)
        
        # 视频 编号
        number = res['data']['number']
        # 视频 标题
        title = res['data']['title']
        #  帖子封面 图片 网址
        cover = res['data']['cover']
        # 帖子封面 转 img格式
        content = f"<img src=\"{cover}\" />"

        # 提取 视频 截图 ，图片链接列表
        screenshots = res['data']['screenshots']

        # 将图片链接列表转换成指定格式的 HTML 字符串
        html_content = ''.join([f"<img src=\"{url}\" />" for url in screenshots])

        # 打印转换后的 HTML 字符串
        # print(html_content)
            
        return number, title, content ,html_content

    return None


def display_json(response):

    # 解析JSON响应内容
    json_data = response

    # 将JSON数据格式化输出，保持人类可读性
    formatted_json = json.dumps(json_data, indent=4, ensure_ascii=False)

    print("响应内容：\n")
    # print(formatted_json)


torrent_path = input("input video path:")

# 获取种子信息
torrent_name = torrent_path.split("/")[-1]

# 获取 jav 信息
jav_info = get_jav_info(torrent_name)

number, title, content, img_shot = jav_info

print(number + '\n\n' + title + '\n')

print("cover pic link:" + content  + '\n\n' + "video shot:" + img_shot)
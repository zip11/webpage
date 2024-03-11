import json
import subprocess
from datetime import datetime

# SOCKS5 代理地址
proxy_address = "socks5://192.168."

# 切割 json
def keep_json_data(num, json_data):

    # 获取用户输入的数量
    user_input = input("请输入要保留的数量：")
    try:
        num = int(user_input)
    except ValueError:
        print("输入的数量不是有效的整数，请重新输入。")
        return

    # 保留指定数量的数据
    kept_data = json_data[:num]
    
    # 打印保留后的数据
    print(kept_data)

    return kept_data


# 获取当前日期
current_date = datetime.now().strftime("%Y-%m-%d")

# 读取 JSON 文件
json_filename = f'video_links_{current_date}.json'

with open(json_filename, 'r', encoding='utf-8') as f:
    video_data = json.load(f)

# 切割 json
video_data = keep_json_data(video_data)

# 使用 yt-dlp 下载视频
for video in video_data:

    url = video['href']
    title = video['title']

    print(f'Downloading: {title}')
    subprocess.run(['yt-dlp',"--extract-audio", "--audio-format", "mp3", "--proxy", proxy_address, url])

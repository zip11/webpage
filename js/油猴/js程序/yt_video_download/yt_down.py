import json
import subprocess
from datetime import datetime

# SOCKS5 代理地址
proxy_address = "socks5://192.168.2.7:20170"


# 获取当前日期
current_date = datetime.now().strftime("%Y-%m-%d")

# 读取 JSON 文件
json_filename = f'video_links_{current_date}.json'

with open(json_filename, 'r', encoding='utf-8') as f:
    video_data = json.load(f)

# 使用 yt-dlp 下载视频
for video in video_data:

    url = video['href']
    title = video['title']

    print(f'Downloading: {title}')
    subprocess.run(['yt-dlp',"--extract-audio", "--audio-format", "mp3", "--proxy", proxy_address, url])

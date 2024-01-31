import json

import requests

import os

# json转m3u
def json_to_m3u(json_data, m3u_file_name):

    # 将 JSON 数据解析为 Python 字典
    data = json.loads(json_data)

    # 指定输出的 M3U 文件路径
    output_file_path = m3u_file_path

    # 打开 M3U 文件并写入播放列表
    with open(output_file_path, 'w') as m3u_file:
        # 写入 M3U 文件的头部
        m3u_file.write("#EXTM3U\n")

        # 遍历频道列表，写入每个频道的流媒体链接
        for channel in data['radios']:
            for stream in channel['streams']:

                # 判断 stream['streamName'] == "高品质"
                if stream['streamName'] == "高品质":
                    m3u_file.write(f"#EXTINF:-1,{channel['channelName']} - {stream['streamName']}\n")
                    m3u_file.write(f"{stream['url']}\n")

    print(f"M3U 文件已创建：{output_file_path}")

# 获取当前脚本的路径
script_path = os.path.abspath(__file__)
print(f"当前脚本路径: {script_path}")

# 获取当前脚本所在目录
script_dir = os.path.dirname(script_path)
print(f"当前脚本所在目录: {script_dir}")


# 下载json
url = 'https://www.cnr.cn/css2017/js/flash/streams.json'
response = requests.get(url)
response.raise_for_status()

# 保存json 文件
with open('radios.json', 'w', encoding='utf-8') as f:
    json_data = response.text
    f.write(json_data)

# 读取json文件
with open('radios.json', 'r', encoding='utf-8') as f:
    json_data2 = f.read()
    print(json_data2)

# m3u 路径
m3u_file_path = os.path.join(script_dir, 'radios.m3u')

# 创建m3u
json_to_m3u(json_data2,m3u_file_path)





def find_channel(json_data,target_channel_name):

    # 将 JSON 数据解析为 Python 字典
    data = json.loads(json_data)

    # 读取特定频道信息（例如"中国之声"）
    target_channel_name = "中国之声"

    # 遍历频道
    for channel in data['radios']:
        
        # 判断 频道，名称
        if channel['channelName'] == target_channel_name:
            
            print(f"频道名称: {channel['channelName']}")
            print(f"描述: {channel['description']}")
            print("流媒体链接:")

            for stream in channel['streams']:
                print(f"  {stream['streamName']}: {stream['url']}")
            break
    else:
        print(f"未找到名称为 '{target_channel_name}' 的频道。")
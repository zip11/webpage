#!/usr/bin/env python3
import subprocess
import os
import json
from datetime import datetime

# 获取 yt-dlp 程序的完整路径
def get_ytdlp_path(folder_path, program_name):

    return os.path.join(folder_path, program_name)

# 加载代理设置
def load_proxy_settings(file_path):

    with open(file_path) as f:
        proxy = json.load(f)
    return proxy["proxy_address"], proxy["proxy_port"]

# 加载 JSON 文件内容
def load_json_content(file_path):

    with open(file_path) as f:
        return json.load(f)

# 下载视频
def download_videos(ytdlp_path, download_directory, proxy_address, proxy_port, json_content):
 
    total = len(json_content)

    # 遍历 JSON 文件中的网址
    for i, item in enumerate(json_content, start=1):

        url = item["url"]
        print(f"Downloading {url}...")

        # 运行 yt-dlp 命令来下载视频
        subprocess.run([
            ytdlp_path,
            "--output", f"{download_directory}/%(title)s.%(ext)s",
            "--format", "best[height<=720]",
            "--proxy", f"socks5://{proxy_address}:{proxy_port}",
            url
        ], shell=True)

        print(f"Downloaded {i} of {total}")

# 保存下载记录
def save_download_record(json_file_path):

    # 生成新的文件名，带有日期前缀
    date_string = datetime.now().strftime("%Y%m%d")

    # 获取文件名（不带扩展名）
    file_name_without_extension = os.path.splitext(os.path.basename(json_file_path))[0]

    # 构建新的文件路径
    new_file_name = f"{date_string}_{file_name_without_extension}"

    # 获取文件所在目录
    new_file_path = os.path.join(os.path.dirname(os.path.abspath(json_file_path)), new_file_name)

    # 复制文件并保存
    with open(json_file_path, 'rb') as fsrc, open(new_file_path, 'wb') as fdst:
        fdst.write(fsrc.read())

    print(f"Saved download record as {new_file_path}")

# 主函数
def main():

    # yt-dlp 程序的文件夹路径
    ytdlp_folder = r"/home/*/app/net/yt-dlp"
    ytdlp_program = "yt-dlp_linux_armv7l"

    # 设置下载目录
    ytdlp_download_folder = r"/home/*/pt/yt-dlp"

    # 设置下载目录
    download_directory = os.path.join(ytdlp_download_folder, "Ph")

    # 确保下载目录存在
    if not os.path.exists(download_directory):

        print("Creating download directory...")
        os.makedirs(download_directory)

    # 读取代理设置的 JSON 文件路径
    proxy_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "proxy.json")

    # 读取 JSON 文件中的网址
    json_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "bookmarks.json")

    # 获取 yt-dlp 程序路径
    ytdlp_path = get_ytdlp_path(ytdlp_folder, ytdlp_program)
    
    # 加载代理设置
    proxy_address, proxy_port = load_proxy_settings(proxy_file)

    # 加载 JSON 文件内容
    json_content = load_json_content(json_file)

    # 下载视频
    download_videos(ytdlp_path, download_directory, proxy_address, proxy_port, json_content)
    print("All downloads completed.")

    # 保存下载记录
    save_download_record(json_file)

    input("Press Enter to continue...")

# 确保主函数在脚本被直接运行时执行
if __name__ == "__main__":

    main()

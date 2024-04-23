import datetime
import json
import os
import re
import requests

# 处理文件名中的特殊字符
def sanitize_filename(filename):
    # 定义要替换的特殊字符列表
    special_chars = r'[\[\]\\\|\/\:\*\?\"\<\>\|]'
    # 使用正则表达式将特殊字符替换为下划线
    return re.sub(special_chars, '_', filename)

# 下载文件函数
def download_file(url, save_path):
    try:
        # 下载文件
        response = requests.get(url, stream=True)
        total_size = int(response.headers.get('content-length', 0))
        downloaded_size = 0

        # 保存文件
        with open(save_path, 'wb') as file:
            for data in response.iter_content(chunk_size=1024):
                file.write(data)
                downloaded_size += len(data)

                # 计算下载进度
                progress = int(downloaded_size / total_size * 100)
                print(f'\r已下载 {downloaded_size}/{total_size} 字节 ({progress}%)', end='', flush=True)

        print(f"\n文件 {save_path} 下载完成")

    # 错误显示
    except requests.exceptions.HTTPError as errh:
        print ("Http Error:", errh)
    except requests.exceptions.ConnectionError as errc:
        print ("Error Connecting:", errc)
    except requests.exceptions.Timeout as errt:
        print ("Timeout Error:", errt)
    except requests.exceptions.RequestException as err:
        print ("OOps: Something Else", err)

# 主函数
def main():
    print("pt-fsm,rss下载链接，开始下载...")

    # 获取py文件所在文件夹
    path = os.path.dirname(__file__)

    # 生成 ${year}${month}${day}_filedown.json
    now = datetime.datetime.now()
    filename = now.strftime("%Y%m%d") + "_filedown.json"

    # json全路径
    data_file = os.path.join(path, filename)

    # 生成 日期字符串，年_月_日
    date_str = now.strftime("%Y_%m_%d")
    # 下载文件夹 全路径
    down_folder = os.path.join(path, 'dwon_file', date_str)

    # dwon_file 文件夹是否存在，不存在创建文件夹
    if not os.path.exists(down_folder):
        os.makedirs(down_folder)
        print(f"文件夹 {down_folder} 创建完成")

    # 读取JSON数据
    with open(data_file, 'r', encoding='utf-8') as file:
        json_data = file.read()

    print(f"读取json文件: {data_file} -完成！！！")

    # 将JSON字符串转换为Python对象（列表）
    data = json.loads(json_data)

    # 遍历数据中的每一项
    for i, item in enumerate(data, start=1):
        title = item['title']
        url = item['url']
        print(f"标题: {title}\n网址: {url}\n")
        print(f"current_number:{i} / total_number:{len(data)}")

        # 处理文件名中的特殊字符
        title = sanitize_filename(title)
        # 下载文件 全路径
        down_file = os.path.join(down_folder, title + ".torrent")

        # 下载文件
        download_file(url, down_file)

    print("下载完成")

# 确保主函数在脚本被直接运行时执行
if __name__ == "__main__":
    main()

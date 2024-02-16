import datetime
import json
import requests

# 下载文件函数
def download_file(url, save_path):

    try:

        # 下载文件 
        response = requests.get(url, stream=True)

        # 保存文件
        with open(save_path, 'wb') as file:
            
            downloaded_size = 0

            for data in response.iter_content(chunk_size=1024):

                file.write(data)
                downloaded_size += len(data)
                print(f'已下载 {downloaded_size} 字节')

        print(f"文件 {save_path} 下载完成")

    # 错误显示
    except requests.exceptions.HTTPError as errh:
        print ("Http Error:",errh)
    except requests.exceptions.ConnectionError as errc:
        print ("Error Connecting:",errc)
    except requests.exceptions.Timeout as errt:
        print ("Timeout Error:",errt)
    except requests.exceptions.RequestException as err:
        print ("OOps: Something Else",err)


# 假设json数据存储在一个字符串变量中
# json_data = '[{"title": "网站A", "url": "http://www.example1.com"}, {"title": "网站B", "url": "http://www.example2.com"}]'

# start ~~~~~~

print("pt-fsm,rss下载链接，开始下载...")


import os
# 获取py文件所在文件夹
path = os.path.dirname(__file__)

# 生成 ${year}${month}${day}_filedown.json
now = datetime.datetime.now()
filename = now.strftime("%Y%m%d") + "_filedown.json"

# json全路径
data_file = os.path.join(path, filename)

# 下载文件夹 全路径
down_folder = os.path.join(path, 'dwon_file')

# dwon_file 文件夹是否存在，不存在创建文件夹
if not os.path.exists(down_folder):

    os.makedirs(down_folder)
    print(f"文件夹 {down_folder} 创建完成")


# 或者从文件中读取JSON数据
with open(data_file, 'r', encoding='utf-8') as file:
    json_data = file.read()

print(f"读取json文件: {data_file} -完成！！！")

# 将JSON字符串转换为Python对象（列表）
data = json.loads(json_data)

i = 1;
# 遍历数据中的每一项
for item in data:

    title = item['title']
    url = item['url']
    print(f"标题: {title}\n网址: {url}\n")

    # 显示 下载进度
    print(f"current_number:{i} / total_number:{len(data)}")
    i = i + 1;

    # 下载文件 全路径
    down_file = os.path.join(down_folder,title + ".torrent")

    # 下载函数
    download_file(url, down_file)
    
    # 只 取一次数据
    # if "兔子" in title:
    #     download_file(url, title + ".torrent")
        
    #     break

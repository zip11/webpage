# fsm自动发种脚本(jav) by orance

import requests
import os
import time
import shutil
import json

# API 地址和密钥
URL = "https://api.fsm.name"

# 你的APITOKEN
APITOKEN = ""

success_count = 0
# 你的种子目录
seed_adree = "./jav_seed"  

# 新 下载种子 的 文件夹
new_seed = "./jav_seed/new_dl"  

# 获取 jav 信息
def get_jav_info(torrent_name):

    res = requests.get(f"https://javdb.fsm.name/Movies/{torrent_name}").json()
    
    # 获取 返回值 结果
    if res.get('success'):
        
        # 视频 编号
        number = res['data']['number']
        # 视频 标题
        title = res['data']['title']
        #  帖子 封面
        cover = res['data']['cover']
        # 帖子 内容
        content = f"<img src=\"{cover}\" />"
    
        return number, title, content

    return None


# 发布 jav 种子
def publish_jav_torrent(torrent_path):
    
    # 获取种子信息
    torrent_name = torrent_path.split("/")[-1]

    # 获取 jav 信息
    jav_info = get_jav_info(torrent_name)    
    
    if jav_info is None:
        print(f"种子 {torrent_name} fsm信息库中无此番号")
        return False
    
    number, title, content = jav_info
    
    # 读取 种子文件
    files = {'torrentFile': open(torrent_path, 'rb')}

    # 帖子 数据
    data = {
        'type': 1,  # 类型为1
        'title': f"{number} {title}",  # 标题
        'content': content
    }


    print("upload torrent start")

    # 上传 post
    headers = {'APITOKEN': APITOKEN}
    response = requests.post(f"{URL}/Torrents/newSubmit", data=data, files=files, headers=headers)

    # 判断 返回 结果
    if response.status_code == 200:

        result = response.json()

        if result.get('success'):
            
            print(f"种子 {torrent_name} 发布成功！")  
            # 输出种子名称

            # print(result)

            # 将 JSON 数据转换为 Python 字典
            data_dict = result

            # 格式化为人类可读的形式并打印
            formatted_json = json.dumps(data_dict, indent=4, ensure_ascii=False)
            print(formatted_json)

            # 从字典中提取 tid 值
            tid = data_dict['data']['tid']

            # 下载种子 全路径
            new_seed_path = os.path.join(new_seed,torrent_name,".torrent")
            # 下载种子
            down_torrent(tid,new_seed_path)

            return True
        else:
            
            print(f"种子 {torrent_name} 发布失败:", result.get('msg'))  
            # 输出种子名称和失败信息
            return False
    else:
        print("请求失败")
        return False

# 下载 种子文件，包含 tracker passkey
def down_torrent(url,save_path):

    try:
        # 发起 GET 请求以获取文件内容
        response = requests.get(url)

        # 检查响应状态码是否为成功状态
        if response.status_code == 200:

            # 打开文件并写入响应内容
            with open(save_path, 'wb') as file:
                file.write(response.content)
            print(f"文件已保存到：{save_path}")
        else:
            # 如果响应状态码不是 200，则打印错误信息
            print(f"下载失败，HTTP 状态码：{response.status_code}")
    except Exception as e:
        # 捕获异常并打印错误信息
        print(f"下载出错：{e}")


# ~~~~~~~~ START ~~~~~~~~~

# 遍历种子目录
for file in os.listdir(seed_adree):

    # 判断 文件 扩展名
    if file.endswith(".torrent"):
        
        # 种子文件 拼接 全路径
        torrent_path = os.path.join(seed_adree, file)
        
        # 发布种子并移动到对应目录
        if publish_jav_torrent(torrent_path):
            
            success_count += 1
            target_folder = seed_adree + "/finish"  
            # 移动到当前目录的/finish文件夹下
        else:
            target_folder = seed_adree + "/failed"  
            # 移动到当前目录的/fail文件夹下  

        # 创建文件夹
        if not os.path.exists(target_folder):
            os.makedirs(target_folder)

        # 移动文件
        shutil.move(torrent_path, target_folder)
        
        if success_count >= 5:  
            # 暂定一次只发5种，根据上行自行调整
            break
        
        time.sleep(5)  
        # 站点要求:API 频率限制为：每分钟 15 次

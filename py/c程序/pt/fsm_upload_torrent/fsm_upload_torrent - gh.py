# fsm自动发种脚本(jav) by orance

import requests
import os
import time
import shutil

# API 地址和密钥
URL = "https://api.fsm.name"
APITOKEN = ""  # 你的APITOKEN
success_count = 0
seed_adree = "./jav_seed"  # 你的种子目录

# 获取 jav 信息
def get_jav_info(torrent_name):

    res = requests.get(f"https://javdb.fsm.name/Movies/{torrent_name}").json()
    
    if res.get('success'):
    
        number = res['data']['number']
        title = res['data']['title']
        cover = res['data']['cover']
        content = f"<img src=\"{cover}\" />"
    
        return number, title, content

    return None


# 发布 jav 种子
def publish_jav_torrent(torrent_path):
    
    # 获取种子信息
    torrent_name = torrent_path.split("/")[-1]
    jav_info = get_jav_info(torrent_name)    
    
    if jav_info is None:
        print(f"种子 {torrent_name} fsm信息库中无此番号")
        return False
    
    number, title, content = jav_info
    
    files = {'torrentFile': open(torrent_path, 'rb')}

    data = {
        'type': 1,  # 类型为1
        'title': f"{number} {title}",  # 标题
        'content': content
    }

    headers = {'APITOKEN': APITOKEN}
    response = requests.post(f"{URL}/Torrents/newSubmit", data=data, files=files, headers=headers)

    if response.status_code == 200:

        result = response.json()

        if result.get('success'):
            
            print(f"种子 {torrent_name} 发布成功！")  
            # 输出种子名称
            return True
        else:
            
            print(f"种子 {torrent_name} 发布失败:", result.get('msg'))  
            # 输出种子名称和失败信息
            return False
    else:
        print("请求失败")
        return False


# 遍历种子目录
for file in os.listdir(seed_adree):

    if file.endswith(".torrent"):
        
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

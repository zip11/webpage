import os


# 获取文件夹下 *.torrent 文件列表
def get_torrent_files(directory):
    
    torrent_files = []

    for root, dirs, files in os.walk(directory):

        for file in files:
            if file.endswith(".torrent"):
                torrent_files.append(os.path.join(root, file))
                
    return torrent_files

# 读取的种子文件名字 list，遍历提取不含扩展名的文件名，提取文件名的部分，
# 再正则提取 部分 文件名是可变的,例如abcd-1234
import re


def extract_file_parts(torrents):
    """
    从种子文件名列表中提取文件名的特定部分，并返回提取的部分组成的列表。
    
    参数：
    - torrents: 包含种子文件名的列表
    
    返回值：
    - 包含提取的文件名部分的列表
    """
    # 定义正则表达式，匹配文件名中的特定部分
    pattern = r'([a-zA-Z]+-\d+)'
    
    # 存储提取的文件名部分
    file_parts = []
    
    # 遍历种子文件名列表，提取文件名中的特定部分
    for filename in torrents:
        match = re.search(pattern, filename)
        if match:
            file_parts.append(match.group(1))
    
    return file_parts

def save_file_parts(file_parts, filename):

    """
    将提取的文件名部分保存到指定的文件中。
    
    参数：
    - file_parts: 包含提取的文件名部分的列表
    - filename: 保存文件的路径
    """
    import json

    with open(filename, 'w') as f:

        # 将文件名部分列表转换为JSON格式，json人类可视化，并写入文件
        json.dump(file_parts, f, indent=4)

    print("文件名部分已保存到file_parts.json文件中。")

# 键盘输入 文件夹路径
directory = input("请输入文件夹路径：")

# 获取文件夹下所有种子文件
torrent_files = get_torrent_files(directory)

# 提取种子文件名中的特定部分
file_parts = extract_file_parts(torrent_files)

# 打印提取的文件名部分
for part in file_parts:
    print(part)

# 保存提取的文件名部分到json文件    
save_file_parts(file_parts, "file_parts.json")

 

    


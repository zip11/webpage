#!/usr/bin/python3
# -*- coding: UTF-8 -*-

import os

# "保存 视频 子文件夹， 全路径 到 sh"

# 获取 子文件夹 路径
def get_subfolders_paths(folder_path):

    # 初始化一个列表来存储子文件夹的全路径
    subfolders_paths = []
    
    # 遍历指定文件夹下的所有子文件夹
    for root, dirs, files in os.walk(folder_path):

        # 遍历 目录
        for dir_name in dirs:

            # 子文件夹 全路径 拼接
            subfolder_path = os.path.join(root, dir_name)
            # 路径 添加到  列表
            subfolders_paths.append(subfolder_path)
    
    # 返回 路径 列表
    return subfolders_paths


print("保存 子文件夹 全路径 到 txt")

folder_path = input("请输入文件夹路径：")

# 指定文件夹路径
# folder_path = 'path/to/your/folder'  # 替换为你的文件夹路径

# 获取子文件夹的全路径列表
subfolders_paths = get_subfolders_paths(folder_path)

# 将子文件夹的全路径保存到txt文件
with open('run_flv_to_mp3.sh', 'w', encoding='utf-8') as file:

    # 文件头， 保存 py 路径
    file.write("flvapp=''\n")
    
    # 遍历 路径
    for path in subfolders_paths:
        file.write("$flvapp " + path + '\n')

print(f'Subfolders paths have been saved to subfolders_paths.txt')
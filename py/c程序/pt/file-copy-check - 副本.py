#!/usr/bin/python3
# -*- coding: UTF-8 -*-

# 提取 原始文件夹的文件 没有移动 -到新文件夹 的 文件名

import os
import shutil

# 原始 文件夹 路径
ys_path = r'M:\p'




#  没有移动 文件 列表
wu_file = []

# 排除复制 文件
ex_file = ["ink","pt-c","torrent","exclude.txt","copy - ts.bat"]


print("提取 原始文件夹的文件 没有移动, -到新文件夹 的 文件名")

# 新 文件夹 路径
n_path = input(" 第二个有复制 文件夹 路径")

# 第三个 复制 文件夹
n2_path = input("第三个 复制 文件夹")

# ---  获取没有复制 文件 列表  st
# 原始 文件 列表
ys_file = os.listdir(ys_path)

# 新文件夹 列表 
n_file = os.listdir(n_path)

# 遍历 原始 文件名
for i in ys_file:

    # 判断 没有 移动 新文件夹 的文件
    if i not in n_file:

        # 判断 排除 复制文件
        if i not in ex_file:
            # 添加 新文件 列表
            wu_file.append(i)
        

print("wu-file:",wu_file)
# ----end----


#  没有复制的 文件 -遍历----st


# 复制 文件 到的 → 新文件夹


for wfile in wu_file:

    # old file 全路径
    o_file = os.path.join(ys_path,wfile)

    # new file  
    new_file = os.path.join(n2_path,wfile)

    # 判断 目录
    if os.path.isdir(wfile):
        shutil.copytree(o_file,new_file)
    
        # 判断 文件  os.path.isfile(wfile)
    else :
        
        # 判断 文件 是否 存在
        if os.path.exists(new_file) != True:
            
            # file copy
            print("copy-start:",new_file)
            shutil.copyfile(o_file,new_file)
        else:
            # 文件 存在
            print("file cun zai",new_file)
   
# --end ---

print("copy file end")
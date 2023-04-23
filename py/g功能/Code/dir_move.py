#!/usr/bin/python3
# -*- coding: UTF-8 -*-

import os
import shutil

# 检查 快捷方式 字符串
def check(string, sub_str): 

    if (string.find(sub_str) == -1): 
        
        #print("不存在！")
        return False

    else: 
        print("存在！") 
        return True

# 文件夹 前缀
txt_del = "picnc"

# 新文件夹 目录
n_dir = r"Y:\1"

print("移动文件夹,文件夹前缀nc")

# 获取 文件夹 下 文件 列表
delink = os.listdir("./")

# print(delink)

for i in delink:

    # 判断 是否目录
    if (os.path.isdir(i)):

        # 检查 文件名 存在 指定前缀
        if check(i,txt_del):

            print("move-dir:",i)

            # 获取 文件名
            wjm = os.path.basename(i)

            # 新 文件夹 路径
            wjm = os.path.join(n_dir,wjm)

            # 移动文件夹
            shutil.move(i,wjm)
        

print("移动文件夹-完成 end")

os.system("pause")
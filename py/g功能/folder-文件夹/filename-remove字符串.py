#!/usr/bin/python3
# -*- coding: UTF-8 -*-

import os

# 检查 快捷方式 字符串
def check(string, sub_str): 

    if (string.find(sub_str) == -1): 
        
        #print("不存在！")
        return False

    else: 
        print("存在！") 
        return True

txt_del= " - 快捷方式"

print("删除 文件名 -快捷方式 ，字符串")

# 获取 文件夹 下 文件 列表
delink = os.listdir("./")

# print(delink)

for i in delink:

    # 检查 文件名 存在 快捷方式
    if check(i,txt_del):

        print("del-",i)
        # 删除文件名 快捷方式
        os.rename(i,i.replace(txt_del,""))

print("rename file end")
os.system("pause")
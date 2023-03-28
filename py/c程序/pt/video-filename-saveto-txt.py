#!/usr/bin/python
# -*- coding: UTF-8 -*-

# 搜索mp4 保存 txt
import os


# 搜索mp4-文件夹
lj1 = r"./"


# 搜索到-mp4 列表
mp4_file = []

print("search文件夹-mp4，保存 txt")
print("搜索文件夹-",lj1)


# 遍历文件夹
for root, dirs, files in os.walk(lj1, topdown=False):

    # 文件 遍历
    for name in files:

        
        
        if(name.endswith(".mp4")):

            mp4_file.append(name)
            
    
print("mp4-file:",mp4_file)


# -----end -----


# --- txt -- st

f = open("video_name.txt","w")

for line in mp4_file:
    f.write(line+'\n')

f.close()

print("mp4 name save to txt")

# ---end ---


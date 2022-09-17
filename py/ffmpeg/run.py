#!/usr/bin/python3
# -*- coding: UTF-8 -*-

# move *.flv to xz folder ,linux

import os
from os import path


print("*.flv to xz folder ,flv to m4a\n")

#获取 当前 文件夹
ljqd =os.getcwd()


#'move-flv.py' , 绝对路径
ljmove = os.path.join(ljqd,'move-flv.py')
print(ljmove)

# move flv xz folder
os.system(ljmove)


#组合 flv-to-aac.py 绝对路径
ljaac = os.path.join(ljqd,'xz','flv-to-aac.py')
print(ljaac)

# mp4 to m4a
os.system(ljaac)


print(" flv to m4a  end !!! ")



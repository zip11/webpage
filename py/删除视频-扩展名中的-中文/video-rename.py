#!/usr/bin/python3
# -*- coding: UTF-8 -*-

# del file chinese ,my这k这v

import os
import re

# folder name
path = r"P:\xz_4t2\11-22-2022\PPPD 667-999"

# change dir
os.chdir(path)

for file_name in os.listdir(path):
    
    #123 ,mkv
    nwjm ,kzm = os.path.splitext(file_name)

    # del chinese
    kzm = re.sub(r"[\u8814]", "",kzm)
    

    # make new file name
    new_name = nwjm + kzm
    
    print(file_name)

    
    # rename 
    os.rename(file_name,new_name)



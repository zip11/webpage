#!/usr/bin/python3
# -*- coding: UTF-8 -*-

#阿里云盘 手机日志log文件，提取token

import re

# read log

loglj = input("input alidrive log file:")

with open(loglj,'r',encoding='utf-8',errors='ignore') as inputdata:
	contents=inputdata.readlines()

# txt 每一行内容
for mh in contents:
    
    # seach token,no
    if mh.find("refreshToken")==-1:

        # list   index
        cnum=contents.index(mh)

        #del list
        del contents[cnum]
    else:

        # search token ok
        print("token-txt:",mh)
        tokentxt=mh

# 
# "refreshToken":"
#print(tokentxt)


# re  token
array1 = re.search(r"\"refreshToken\"\:\"(\w*)\"", tokentxt)

# object to str
tkre=str(array1.group(1))

print(tkre,type(tkre))


# clipboard
import pyperclip

pyperclip.copy(tkre)
pyperclip.paste()

print("token copy  clip ok")

ex=input("Enter key exit ")
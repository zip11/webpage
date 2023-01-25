#!/usr/bin/python3
# -*- coding: UTF-8 -*-

import re

# read log

with open(r'2023-01-21-19.log','r',encoding='utf-8',errors='ignore') as inputdata:
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

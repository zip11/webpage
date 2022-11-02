#!/usr/bin/python3
# -*- coding: UTF-8 -*-

import codecs

# file utf8 to gbk

def ReadFile(filePath,encoding="utf-8"):
    with codecs.open(filePath,"r",encoding) as f:
        return f.read()
 
def WriteFile(filePath,u,encoding="gb18030"):
    with codecs.open(filePath,"w",encoding) as f:
        f.write(u)
 
def UTF8_2_GBK(src,dst):
    content = ReadFile(src,encoding="utf-8")
    WriteFile(dst,content,encoding="gb18030")

ilj = input("pz.ini utf8 to gb18030 ")

UTF8_2_GBK(ilj,ilj)
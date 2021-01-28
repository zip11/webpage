import os
import linecache
import re


def updateFile(file,old_str,new_str):
    """
    替换文件中的字符串
    :param file:文件名
    :param old_str:旧字符串
    :param new_str:新字符串
    :return:
    """

        
    f = open(file, "r", encoding="gb2312")
    f_new = open("hosts1.txt", "w", encoding="gb2312")

    for line in f:
        if old_str in line:
            line = line.replace(old_str, new_str,1) + " www.pttime.org"
        f_new.write(line)
    f.close()
    f_new.close()


def search(key_word: str):
#搜索特定字符串，txt在哪行
    with open('hosts.txt') as f:
        for index, line in enumerate(f.readlines()):
            if key_word in line:
                result = index + 1
                break
        else:
            result = -1

    return result
    
def txths(file,hs1):
#取某行内容

    print(hs1)
    i = 0

    with open(file,'r') as f:
        while True:
            line = f.readline()
            i = i + 1
            
            if line:
                if i == hs1:
                    print("读取某行内容",line)
                    return line
            else:
                break

    return line
    
def qip(nr1):
    ##正则提取ip

    regular = '[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}'
    vv = re.search(regular, nr1)
    bb1 = vv.group()
    
    print("正则提取ip",bb1)
    
    return bb1

if __name__ == '__main__':

    cfip = input("input cf ip:")
    #查找ip所在的行数
    hs1 = search("pttime")
    print("搜索内容在",hs1)
    
    #获取指定ip行数 内容
    ip1 = txths('hosts.txt',hs1)
    
    #获取正则ip
    qip(ip1)


        
    updateFile("hosts.txt",ip1,cfip)


import os

wj = []

#删除字符
ts1 = '=[www.zz5100.com]'
ts2 = "== (www.zz5100.com) 微信(zazhiwu)"

path=input('请输入文件路径(结尾加上/)：')       

#获取该目录下所有文件，存入列表中
fileList=os.listdir(path)

#print(fileList)

#删除文件夹
for i in fileList:
    if os.path.isfile(i):
        #print(i)
        wj.append(i)

print(wj)

n=0


for i in wj:
    
    #设置旧文件名（就是路径+文件名）
    oldname=path+ os.sep + wj[n]   # os.sep添加系统分隔符
    
    
    nm = wj[n].replace('\'','')
    nm = nm.replace(ts1,'')
    nm = nm.replace(ts2,'')
    #设置新文件名
    newname=path + os.sep + nm
    
    os.rename(oldname,newname)   
    #用os模块中的rename方法对文件改名
    
    print(oldname,'======>',newname)
    
    n+=1

os.system('pause')
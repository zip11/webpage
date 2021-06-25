import os

#bat文件夹 路径
nlj = ""

#压缩命令
ml1 = ""
#双引号
yh1 = '"'


path=input('请输入 要 压缩文件夹 路径(路径结尾 要 删除\)：')

path1=os.path.join(path)

#获取该目录下所有文件，存入列表中
fileList=os.listdir(path1)


#print(fileList)

n=0
for i in fileList:
    
    #设置文件名（就是路径+文件名）
    oldname=yh1 + path1+ os.sep + fileList[n] + yh1+ " "  
    
    # os.sep添加系统分隔符
    
    

    
    #组成 所有子文件夹 路径
    
    nlj = nlj+oldname

    n+=1

print(nlj)

ml1 = "Bandizip bc -aoa -o:" + path1 + " " + nlj

os.system(ml1)
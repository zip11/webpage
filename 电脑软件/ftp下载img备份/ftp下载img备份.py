import datetime
import os
import sys


#下载目录设置，txt文件里面
wjlj = os.path.split( os.path.realpath( sys.argv[0] ) )[0]

txtlj = wjlj+"\pi3.txt"

print(txtlj)

#os.system("pause")

def xzml():
#生成昨天的文件名 img
    yesterday = (datetime.date.today() + datetime.timedelta(days=-1)).strftime('%Y%m%d')

    print(yesterday,type(yesterday))

    xz = "get " + yesterday +"pi3.img" + "\n"

    #print(xz)
    return xz

def dtxt():
    #读取txt，替换get 命令
    fileHandler  =  open  (txtlj,  "r")
    # Get list of all lines in file

    txtmh  =  fileHandler.readlines()
    # Close file
    fileHandler.close()


    #print(listOfLines)


    #替换 get img 命令
    txtmh[5] =  xzml()

    print(txtmh[5],"xzml")
    return txtmh


listOfLines = dtxt()

#写出 新txt 文件
f = open(txtlj, 'w+')

for i in range(0,len(listOfLines)):
    #print(i,"i=",listOfLines[i])
    f.write(str(listOfLines[i]))    
    
f.close()

#ftp txt run
wcml = 'ftp.exe -s:\"' + txtlj + '\"'

print(wcml)
os.system(wcml)

#ftp end

#delete img

sclj = wjlj +"\del3.bat"
os.system(sclj)

#img end

os.system("pause")

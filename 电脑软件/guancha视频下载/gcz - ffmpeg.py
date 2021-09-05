import os
import time

# temp_name = "【察话会Au】210901施佬和阿怡聊聊坦克两项接力赛和其他大事件" 
   
# os.system("ffmpeg.exe -i " + temp_name  +  ".mp4" + " -vn -codec copy " + temp_name + ".m4a")

# os.system("pause")

print("文件夹视频MP4批量 转换 m4a")

#获取 当前目录
path = os.getcwd()

#获取 所有文件名
fileList=os.listdir(path)

#print(fileList)

n=0

for i in fileList:
    
    oldnm = fileList[n]

    
    #过滤 非mp4
    if(oldnm.find("mp4")!=-1):

        #改名m4a
        nm= fileList[n].replace('mp4','m4a')
        
        

        print(nm)
        
        #转换 m4a
        os.system("ffmpeg.exe -i " +  oldnm + " -vn -codec copy " + nm)

    n = n + 1 
  



os.system("pause")

import requests
import re
import configparser
import time


#yt 2021.06 没有更新了

if __name__ == '__main__':


    cfp = configparser.ConfigParser()
    cfp.read("bbh.ini")

    dl1 = cfp.get("yt", "daili")

    
    #上网代理
    s = requests.session()
  #  s.proxies = {'https': dl1}
    

    
    #下载网址

    wz1 = "https://hub.fastgit.org/github.com/yt-dlp/yt-dlp/releases/latest/download/yt-dlp.exe"
    print("download link",wz1)
    
    
    ##提取网址版本号
    response = requests.get("https://api.github.com/repos/yt-dlp/yt-dlp/releases/latest")

    zxbb = response.json()["tag_name"]
    bb1 = zxbb
    print("网站版本号",bb1)
    


    #读取版本号
    bd1 = cfp.get("yt", "bbh")
    print("ini版本号",bd1)
    
    if bd1 == bb1 :
        print("no download")
        time.sleep(5)
    else:
        #下载软件 开始
        
        #保存新版本号
        cfp.set("yt", "bbh", bb1)
        
        print("download start")
        r = s.get(wz1)
    
        lj2 = cfp.get("yt", "bclj")
        print("下载保存路径",lj2)
        
        with open(lj2, "wb") as f:
            f.write(r.content)
    
        print("download end")
        
        #保存ini
        with open("bbh.ini", "w+") as f:
            cfp.write(f)
    

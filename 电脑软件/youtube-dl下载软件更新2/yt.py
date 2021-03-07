import requests
import re
import configparser
import time


if __name__ == '__main__':


    cfp = configparser.ConfigParser()
    cfp.read("bbh.ini")

    dl1 = cfp.get("yt", "daili")

    
    #上网代理
    s = requests.session()
    s.proxies = {'https': dl1}
    
    #读取网页
    htmls = s.get('https://ytdl-org.github.io/youtube-dl/download.html')
    htmls = htmls.text
    #print(type(htmls))
    #print("web page",htmls)
    
    #正则提取下载网址
    regular = 'https://yt-dl.org/downloads/\d{4}\.\d{2}\.\d{2}\.?\d?/youtube-dl.exe'
    vv = re.search(regular, htmls)
    wz1 = vv.group()
    print("download link",wz1)
    
    
    ##正则提取网址版本号
    regular = '\d{4}\.\d{2}\.\d{2}'
    vv = re.search(regular, wz1)
    bb1 = vv.group()
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
    

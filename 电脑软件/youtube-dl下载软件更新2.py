import requests
import re
 
def dtxt(lj1):
    
    with open(lj1, "r") as f:
        data = f.readline()
        print("txt版本号",data)
        return  data 

def xtxt(lj1,nr1):

    with open(lj1,"w") as f:
        f.write(nr1)

if __name__ == '__main__':
    
    #上网代理
    s = requests.session()
    s.proxies = {'https': 'socks5:192.168.2.7:1200'}
    
    #读取网页
    htmls = s.get('https://ytdl-org.github.io/youtube-dl/download.html')
    htmls = htmls.text
    #print(type(htmls))
    #print("web page",htmls)
    
    #正则提取下载网址
    regular = 'https://yt-dl.org/downloads/\d{4}\.\d{2}\.\d{2}/youtube-dl.exe'
    vv = re.search(regular, htmls)
    wz1 = vv.group()
    print("download link",wz1)
    
    
    ##正则提取网址版本号
    regular = '\d{4}\.\d{2}\.\d{2}'
    vv = re.search(regular, wz1)
    bb1 = vv.group()
    print("网站版本号",bb1)
    
    
    #读取txt版本号
    bd1 = dtxt("bbh.txt")
    
    
    if bd1 == bb1 :
        print("no download")
    else:
        #下载软件 开始
        
        #保存新版本号
        bb1 = xtxt("bbh.txt",bb1)
        
        print("download start")
        r = s.get(wz1)
    
 
        with open(r"K:\youtube-dl.exe", "wb") as f:
            f.write(r.content)
    
        print("download end")
    

import requests
import re
 
if __name__ == '__main__':
    
    #上网代理
    s = requests.session()
    s.proxies = {'https': 'socks5:192.168.2.7:1200'}
    
    #读取网页
    htmls = s.get('https://ytdl-org.github.io/youtube-dl/download.html')
    htmls = htmls.text
    print(type(htmls))
    #print(htmls)
    
    #正则提取下载网址
    regular = 'https://yt-dl.org/downloads/\d{4}\.\d{2}\.\d{2}/youtube-dl.exe'
    vv = re.search(regular, htmls)   
    print(vv.group())
    
    
    #下载软件 开始
    r = s.get(vv.group())
    
    print("download start")
 
    with open(r"K:\tongbu\xz\ytxz\youtube-dl.exe", "wb") as f:
        f.write(r.content)
    
    print("download end")
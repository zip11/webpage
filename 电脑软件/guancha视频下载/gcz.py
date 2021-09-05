from bs4 import BeautifulSoup

import requests

import time


def wybt(wz):
    #获取 网页 标题
    #url = 'https://user.guancha.cn/main/content?id=575808&v=1630823848952'
    html = wz 




    soup = BeautifulSoup(html,'lxml')

    #获取 article-content
    kj1 = soup.find('div',class_='article-content')
    #print(kj1,type(kj1))

    bt1 = str(kj1.h1.string)


    print(bt1,type(bt1))
    
    return bt1



#url = 'https://user.guancha.cn/main/content?id=575808&v=1630823848952'

url = input("input guancha.cn viedo  link:")

#html = urllib.request.urlopen(url).read()

headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36 Edg/93.0.961.38'}
resp = requests.get(url,headers = headers)
resp.encoding = 'utf-8'
html = resp.text
#print("响应内容", html)


soup = BeautifulSoup(html,'lxml')

#获取iframe
kj1 = soup.find('iframe')
#print(kj1,type(kj1))

#获取src属性
#print("src--",kj1['src'],type(kj1))

wz1 = kj1['src']

wz1 = str(wz1)

print("video player link",wz1,type(wz1))

biaoti1 = wybt(html)

#url = 'https://1251245530.vod2.myqcloud.com/vod-player/1251245530/3701925923760985310/tcplayer/console/vod-player.html?autoplay=false&width=1280&height=720'

url = wz1



# ② 获取视频 网址，需要游览器加载

#edge 无头游览器


from selenium import webdriver
from msedge.selenium_tools import EdgeOptions
from msedge.selenium_tools import Edge

# edge end




edge_options = EdgeOptions()
edge_options.use_chromium = True

# 设置无界面模式，也可以添加其它设置
edge_options.add_argument('headless')


driver = Edge(options=edge_options,executable_path='msedgedriver.exe')

r = driver.get(url)
#print("biao ti",driver.title)


#获取 网页内容
content = driver.page_source

#退出 游览器
driver.quit()

#bs4 转换
soup = BeautifulSoup(content,'lxml')
#video player 网页内容
#print(soup)
kj2 = soup 
#print(kj2)



#获取 video 标签
kj3 = soup.find('video')
kj4 = kj3['src']

print("video down link",kj4)

wzsp = str(kj4)

file_url = wzsp

#下载mp4
headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36 Edg/93.0.961.38'}

r = requests.get(file_url, stream=True,headers = headers)

#下载文件名  基于时间
# wjm1 = time.strftime("%Y-%m-%d %H-%M-%S", time.localtime())
# wjm1 = wjm1 + ".mp4" 

wjm1 = biaoti1

with open(wjm1, "wb") as mp4:
    for chunk in r.iter_content(chunk_size=1024):
        if chunk:
            mp4.write(chunk)

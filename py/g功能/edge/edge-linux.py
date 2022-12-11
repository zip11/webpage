#!/usr/bin/env python3

#edge 无头游览器
from bs4 import BeautifulSoup

from selenium import webdriver
from msedge.selenium_tools import EdgeOptions
from msedge.selenium_tools import Edge

# edge end

# web wait start


# web wait end


import requests





def xzsp(spwz):


    options = EdgeOptions()
    options.use_chromium = True
    options.binary_location = r"/usr/bin/microsoft-edge-dev"
    options.set_capability("platform", "LINUX")
    options.add_argument('no-sandbox')
    options.add_argument('disable-dev-shm-usage')
    options.add_argument('headless')
    options.add_argument('disable-gpu')
    #不禁止gpu，腾讯云 加载网页慢

    webdriver_path = r"/home/ubuntu/app/edge/msedgedriver"
    driver = Edge(options=options, executable_path=webdriver_path)


    r = driver.get(spwz)
    #print("biao ti",driver.title)

    driver.implicitly_wait(5) 
    #设置等待20秒钟



    #获取 网页内容
    content = driver.page_source.encode('utf-8')



    #bs4 转换
    soup = BeautifulSoup(content,'lxml')
    print(soup)
    #kj2 = soup 
    #print(kj2)



    #获取 video 标签
    kj3 = soup.find('video')
    kj4 = kj3['src']

    print(kj4)


    wzsp = str(kj4)

    driver.quit()


    if(wzsp!="") :
    
        file_url = wzsp

        #下载mp4
        headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36 Edg/93.0.961.38'}

        # r = requests.get(file_url, stream=True,headers = headers)

        # with open("1.mp4", "wb") as mp4:
        #     for chunk in r.iter_content(chunk_size=1024):
        #         if chunk:
        #             mp4.write(chunk)
        
        print("dl end ok")
        return file_url

    else :
        return "link space error"


dlwz = ""

hy1=xzsp(dlwz)
print(hy1)
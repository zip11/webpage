# from selenium import webdriver
# driver = webdriver.Edge(executable_path='msedgedriver.exe')
# driver.get('https://www.baidu.com')

#edge 无头游览器
from bs4 import BeautifulSoup

from selenium import webdriver
from msedge.selenium_tools import EdgeOptions
from msedge.selenium_tools import Edge

# edge end

import requests


edge_options = EdgeOptions()
edge_options.use_chromium = True

# 设置无界面模式，也可以添加其它设置
edge_options.add_argument('headless')


driver = Edge(options=edge_options,executable_path='msedgedriver.exe')

r = driver.get('')
#print("biao ti",driver.title)


#获取 网页内容
content = driver.page_source

#退出 游览器
driver.quit()

#bs4 转换
soup = BeautifulSoup(content,'lxml')
print(soup)
kj2 = soup 
#print(kj2)



#获取 video 标签
kj3 = soup.find('video')
kj4 = kj3['src']

print(kj4)

wzsp = str(kj4)

file_url = wzsp

#下载mp4
headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36 Edg/93.0.961.38'}

r = requests.get(file_url, stream=True,headers = headers)

with open("1.mp4", "wb") as mp4:
    for chunk in r.iter_content(chunk_size=1024):
        if chunk:
            mp4.write(chunk)
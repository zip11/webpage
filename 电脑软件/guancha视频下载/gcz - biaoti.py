from bs4 import BeautifulSoup

import requests







# wz1 = kj1['src']

# wz1 = str(wz1)

# print("video player link",wz1,type(wz1))

def wybt(wz):
    #url = 'https://user.guancha.cn/main/content?id=575808&v=1630823848952'
    url = wz 

    #url = input("input guancha.cn viedo  link:")

    #html = urllib.request.urlopen(url).read()

    headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36 Edg/93.0.961.38'}
    resp = requests.get(url,headers = headers)
    resp.encoding = 'utf-8'
    html = resp.text
    #print("响应内容", html)


    soup = BeautifulSoup(html,'lxml')

    #获取iframe
    kj1 = soup.find('div',class_='article-content')
    #print(kj1,type(kj1))

    bt1 = str(kj1.h1.string)


    print(bt1,type(bt1))
    
    return bt1

wybt('https://user.guancha.cn/main/content?id=575808&v=1630823848952')

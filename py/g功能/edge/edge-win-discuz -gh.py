# from selenium import webdriver
# driver = webdriver.Edge(executable_path='msedgedriver.exe')
# driver.get('https://www.baidu.com')

# discuz 登录，保存cookie，
# 读取cookie，检查登录

# edge 无头游览器
from bs4 import BeautifulSoup

from selenium import webdriver
# edge option
from msedge.selenium_tools import EdgeOptions
from msedge.selenium_tools import Edge

# edge end

import requests

# sleep
import time
# cookie save
import pickle

# cookie to dict
def cookietodict(b):
    
    cookie ={}

    for line in b.split(';'):

        key, value = line.split('=', 1)
        cookie[key] = value

    #print(cookie)
    return cookie

# Selenium+phantomJS+Python 操作cookie实现自动登录（以音悦台为例）
# https://blog.csdn.net/mighty13/article/details/78167802


# discuz Login
def login(user,pawd):

    # 
    wz1 = "https://bbs.tampermonkey.net.cn/member.php?mod=logging&action=login"

    r = driver.get(wz1)

    driver.implicitly_wait(10) 
    # 设置等待 * 秒钟

    # login_input=driver.find_elements_by_class_name("login-text-long")
    # driver.find_element_by_id("username_Laddx").send_keys("尚学堂")

    # ~~~web input start ~~~~
    

    # input username
    driver.find_element_by_name("username").send_keys(user)
    # input password
    driver.find_element_by_name("password").send_keys(pawd)

    # keep login
    driver.find_element_by_name("cookietime").click()

    # login button
    driver.find_element_by_name("loginsubmit").click()

    time.sleep(10)

    # ~~~web input end ~~~~

    # ~~~ cookie save start ~~~
    cookie_list = driver.get_cookies()

    #print cookie_list
    print('获得cookie!',type(cookie_list))

    # Cookie File Name
    addtime = time.strftime("%Y-%m-%d %H-%M-%S", time.localtime()) 

    # 以二进制格式打开一个文件只用于写入。如果该文件已存在则将其覆盖。如果该文件不存在，创建新文件
    f = open(addtime + '.cookie', 'wb')
    # Save Cookie
    pickle.dump(cookie_list, f)

    f.close()
    print('cookie文件：'+addtime+'.cookie')

    # ~~~ cookie save End ~~~

def login_by_cookie(cktxt):

    # web link
    wz2="https://bbs.tampermonkey.net.cn/"

    # Cookie File
    cktxt = cktxt + '.cookie'

    driver.get(wz2)
    time.sleep(10)

    # Del Cookie
    driver.delete_all_cookies()

    # Read Cookie
    f = open(cktxt, 'rb')
    # 读取 ， 二进制对象文件转换成 Python 对象
    cookie_set = pickle.load(f)
    
    # Add Cookie
    for i in cookie_set:
        try:
            driver.add_cookie(i)
        except:
            pass

    # Reload page
    driver.get(wz2)

    time.sleep(10)
    
    #url
    print(driver.current_url)

    # file Name
    addtime=time.strftime("%Y-%m-%d %H-%M-%S", time.localtime())

    # screen shot   
    driver.get_screenshot_as_file(addtime+'.png') 


# ~~~ Main ~~~Start ~~~~~~~~~~

edge_options = EdgeOptions()
edge_options.use_chromium = True

# 设置无界面模式，也可以添加其它设置
#edge_options.add_argument('headless')

#--disable-gpu
edge_options.add_argument('disable-gpu')

# ssl_client_socket_impl.cc
edge_options.add_argument('ignore-certificate-errors')

driver = Edge(options=edge_options,executable_path='msedgedriver.exe')



#wz1 = "https://kp.m-team.cc/"


# Discuz Login ,Save Cookie

#login("user","passwd")

# Read Cookie
login_by_cookie("2022-12-10 12-13-54" )


#fill_text(driver,login_input[0],'xxxxx')

#driver.add_cookie(cookie_dict=cookierd)



#print("biao ti",driver.title)


# 获取 网页内容
# content = driver.page_source.encode('utf-8')
# content = driver.page_source

# print(content)

# 退出 游览器
#driver.quit()



# #bs4 转换
# soup = BeautifulSoup(content,'lxml')
# print(soup)
# kj2 = soup 
# #print(kj2)



# #获取 video 标签
# kj3 = soup.find('video')
# kj4 = kj3['src']

# print(kj4)

# wzsp = str(kj4)

# file_url = wzsp


# # ~~~~~下载mp4 ~~start ~~~~~~~

# headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36 Edg/93.0.961.38'}

# r = requests.get(file_url, stream=True,headers = headers)

# with open("1.mp4", "wb") as mp4:
#     for chunk in r.iter_content(chunk_size=1024):
#         if chunk:
#             mp4.write(chunk)

# # ~~~~~~end ~~~~~~~~
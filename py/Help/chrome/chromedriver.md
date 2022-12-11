
浏览器路径：D:\Cent Browser\CentBrowser\Application\chrome.exe

浏览器配置文件路径：C:\Users\wangfan\AppData\Local\CentBrowser\User Data\Default


**下载webdriver**

[https://registry.npmmirror.com/binary.html?path=chromedriver/](https://registry.npmmirror.com/binary.html?path=chromedriver/)


**3.下载浏览器内核**

因为如果使用的是套壳浏览器chrome版本74.0.3729.169，不存在相应内核，所以选择大版本号最相近的即可。

选择对应版本号的驱动非常重要，不然只会使用中会出现无法调用浏览器的情况


**4.之后将解压后的chromedriver.exe放置python所在的根目录即可**


**5.将浏览器所在目录设置到环境变量path中**

配置环境变量:此电脑→右击属性→高级系统设置→环境变量→用户变量→Path→编辑→新建，将以下路径复制,然后不要忘记后续全部点击确定

C:\Program Files (x86)\Google\Chrome\Application\

D:\Program Files\CentBrowser\Application


    from selenium import webdriver
     
    # 个人资料路径（注意路径只到User Data而不是Default）
    user_data_dir = r'--user-data-dir=C:\Users\wangfan\AppData\Local\CentBrowser\User Data'

    # 加载配置数据（根据需求而定，不加配置的话启动的是纯净的浏览器）
    option = webdriver.ChromeOptions()
    option.add_argument(user_data_dir)

    # 启动浏览器配置
    driver = webdriver.Chrome(chrome_options=option)
    driver.get('https://www.baidu.com/')
	# window max
	driver.maximize_window()

 
## start cmd option ##
    
    from selenium.webdriver.chrome.options import Options
    from selenium import webdriver
    chrome_options = Options()

    #加上下面两行，解决报错

    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    chrome_options.add_argument('window-size=1920x3000') #指定浏览器分辨率
    chrome_options.add_argument('--disable-gpu') #谷歌文档提到需要加上这个属性来规避bug
    chrome_options.add_argument('--hide-scrollbars') #隐藏滚动条, 应对一些特殊页面
    chrome_options.add_argument('blink-settings=imagesEnabled=false') #不加载图片, 提升速度
    chrome_options.add_argument('--headless') #浏览器不提供可视化页面. linux下如果系统不支持可视化不加这条会启动失败

    # chrome_options.binary_location = r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe" #手动指定使用的浏览器位置
    
    
    driver=webdriver.Chrome(chrome_options=chrome_options)#executable_path驱动路径
    driver.get('http://www.baidu.com')
    print(driver.page_source)



————————————————
版权声明：本文为CSDN博主「死神萝莉」的原创文章，遵循CC 4.0 BY-SA版权协议，转载请附上原文出处链接及本声明。
原文链接：https://blog.csdn.net/u010741500/article/details/101068167
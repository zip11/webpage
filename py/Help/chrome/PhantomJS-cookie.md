下载软件

[https://phantomjs.org/download.html](https://phantomjs.org/download.html)

PhantomJS安装

[https://blog.csdn.net/qq_41646358/article/details/81543540](https://blog.csdn.net/qq_41646358/article/details/81543540)


PhantomJS从入门 ，js编程

[https://www.jianshu.com/p/8210a17bcdb8](https://www.jianshu.com/p/8210a17bcdb8)

PhantomJS简介

[https://blog.csdn.net/violetgo/article/details/48105593](https://blog.csdn.net/violetgo/article/details/48105593)

phantomJS+Python 操作cookie实现自动登录（以音悦台为例）

[https://blog.csdn.net/mighty13/article/details/78167802](https://blog.csdn.net/mighty13/article/details/78167802)

phantomJS元素定位，鼠标事件

[https://zhuanlan.zhihu.com/p/111859925](https://zhuanlan.zhihu.com/p/111859925)

爬虫Spider 07 - cookie模拟登录 | selenium+phantomjs/Chrome/Firefox

[https://blog.csdn.net/qq_45305211/article/details/102599167](https://blog.csdn.net/qq_45305211/article/details/102599167)


Selenium与PhantomJS 游览器模拟操作 命令
[https://zhuanlan.zhihu.com/p/161449740](https://zhuanlan.zhihu.com/p/161449740)

----------

### UserWarning: Selenium support for PhantomJS has been deprecated, please use headless versions of Chrome or Firefox instead ###


### 二：selenium版本降级 ###

查看当前selenium版本：pip3 show selenium

卸载selenium：pip3 uninstall selenium

安装指定版本：pip3 install selenium==2.48.0


----------

msedge selenium工具3.141.3需要selenium==3.141，但您的selenium 4.7.2不兼容。

pip3 install selenium==3.141



    from selenium import webdriver
    
    driver=webdriver.PhantomJS(executable_path=r'D:\Program Files\Python38\phantomjs-2.1.1\bin\phantomjs.exe')
    driver.get('http://news.sohu.com/scroll/')
    print(driver.find_element_by_class_name('title').text)



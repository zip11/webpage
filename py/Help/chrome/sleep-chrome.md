## 1.强制等待 ##

第一种也是最简单粗暴的一种办法就是强制等待sleep(x),强制让闪电侠等x时间

    from selenium import webdriver
    import time
    
    # 会开会话
    driver = webdriver.Chrome()
    driver.get('http://www.baidu.com')
    
    # 强制等待3秒
    time.sleep(3)
    
    print(driver.current_url)
    driver.quit()

强制等待,不管你浏览器是否加载完,程序都得等待3秒,3秒一到,继续执行下面的代码,不建议经常使用这种强制等待方法

## 2.隐性等待 ##

第二种隐性等待,implicitly_wait(x),整个driver周期有效,x单位秒

    from selenium import webdriver
    
    # 会开会话
    driver = webdriver.Chrome()
    
    # 隐性等待,最长等待30秒
    driver.implicitly_wait(30)
    driver.get('http://www.baidu.com')
    
    print(driver.current_url)
    driver.quit()

隐形等待是设置了一个最长等待时间,如果在规定时间内网页加载完成,则执行下一步,否则一直等到时间截止,然后执行下一步.注意这里有一个弊端,那就是程序会一直等待整个页面加载完成,也就是一般情况下你看到浏览器标签栏那个小圈不再转,才会执行下一步,但有时候页面想要的元素早就在加载完成了,但是因为个别js之类的东西特别慢,我仍得等到页面全部完成才能执行下一步

## 3.显性等待 ##

第三种办法就是显性等待,WebDriverWait,配合该类的until()和until_not()方法,就能够根据判断条件而进行灵活地等待了.它主要的意思就是:程序每隔x秒看一眼,如果条件成立了,则执行下一步,否则继续等待,直到超过设置的最长时间,然后抛出TimeoutException

    from selenium import webdriver
    from selenium.webdriver.support.wait import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC
    from selenium.webdriver.common.by import By
    
    # 会开会话
    driver = webdriver.Chrome()
    driver.get('http://www.baidu.com')
    
    driver.find_element_by_id('kw').send_keys('selenium')
    driver.find_element_by_id('su').click()
    
    # 显性等待
    WebDriverWait(driver,20).until(EC.visibility_of_element_located((By.XPATH,'//a[text()=" - Web Browser Automation"]')))
    driver.find_element_by_xpath('//a[text()=" - Web Browser Automation"]').click()
    
    print(driver.current_url)
    driver.quit()

我们设置了隐性等待和显性等待,在其他操作中,隐性等待起决定性作用,在WebDriverWait..中显性等待起主要作用,但要注意的是:最长的等待时间取决于两者之间的大者,此例中为20,如果隐性等待时间>显性等待时间,则该句代码的最长等待时间等于隐性等待时间
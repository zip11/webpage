# 点击-选择-元素操作 #


----------


# checkbox 方形-检查框

    driver.find_element_by_xpath('//input[@value="cv1"]').click()  
    # click

    driver.find_element_by_xpath('//input[@value="cv2"]').send_keys(Keys.SPACE)  
    # send space

# radio 圆圈-检查框

    driver.find_element_by_xpath('//input[@value="rv1"]').send_keys(Keys.SPACE)  
	# send space
    sleep(1)

    driver.find_element_by_xpath('//input[@value="rv2"]').click()  
	# click


## 检查某个框是否被选中 ##

**element.is_selected()**

    if driver.find_element_by_xpath('//input[@value="rv1"]').is_selected():
    	print 'selected!'
    else:
    	print 'not yet!'

————————————————
版权声明：本文为CSDN博主「huilan_same」的原创文章，遵循CC 4.0 BY-SA版权协议，转载请附上原文出处链接及本声明。
原文链接：https://blog.csdn.net/huilan_same/article/details/52287955
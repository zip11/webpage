# 元素定位 #
打开开发者工具：F12 或者是点击鼠标右键选择 检查 按钮。

总共2类8种方法

driver.find_element_by_xxx() 
1
如果匹配到多个，则返回匹配到的第一个。
如果匹配不到，则抛出NoSuchElementException异常（报错）。

## 1、ID 通过元素的id属性来定位元素 ##

id 通过元素的ID属性来定位元素

driver.find_element_by_id("IamID").send_keys("通过元素的ID属性来定位元素")


## 2、name 通过元素的name属性来定位元素 ##

name 通过元素的name属性来定位元素

driver.find_element_by_name("first").send_keys("通过元素的name属性来定位元素")


## 3、class_name 通过元素的class属性来定位元素 ##

class_name 通过元素的class属性来定位元素

driver.find_element_by_class_name("poem").send_keys("通过元素的class属性来定位元素")

如果class属性值中有空格，则可以截取class属性的部分值（截取到的部分值中一定不要包含空格）

driver.find_element_by_class_name("Dream").send_keys("通过部分值来定位元素")


## 4、tag_name 通过标签的标签名来定位元素 ##

tag_name 通过标签的标签名来定位元素

print (driver.find_element_by_tag_name("a").text)

## 5、link_text 根据 超链接 标签中的文本内容来定位元素 只对a标签是有效 ##

link_text 根据 超链接标签 中的文本内容来定位元素

print (driver.find_element_by_link_text("唐•李白").text)
print (driver.find_element_by_link_text("唐•李白").get_attribute("value"))

## 6、partial_link_text 根据 超链接标签 中的 部分文本来定位元素 ##

partial_link_text 根据 超链接标签中的 部分文本 来定位元素*

print (driver.find_element_by_partial_link_text("唐").text)

## 7、css selector 根据 css选择器 来定位元素 ##

简单用法
在开发者工具中，选中要定位的元素，点击鼠标右键，选择Copy，选择Copy selector，这样就表示copy到了css 选择器。
Chrome浏览器获取css选择器的过程，如下图所示：


## 8、xpath 根据 xpath表达式 来定位元素 ##

xpath 根据 xpath表达式来定位元素

driver.find_element_by_xpath('//*[@id="IamID"]').send_keys("根据 xpath表达式来定位元素")

**简单用法**

在开发者工具中，选中要定位的元素，点击鼠标右键，选择Copy，选择xpath，这样就表示copy到了xpath表达式。
Chrome浏览器获取xpath表达式的过程，如下图所示：

————————————————
版权声明：本文为CSDN博主「@chameleon」的原创文章，遵循CC 4.0 BY-SA版权协议，转载请附上原文出处链接及本声明。
原文链接：https://blog.csdn.net/weixin_56349063/article/details/121761073
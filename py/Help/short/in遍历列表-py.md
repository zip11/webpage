# in 在python中的使用很常见 #

---

## 在 for 循环中，获取列表或者元组的每一项： ##

    for item in list:


## 判断左边的元素是否包含于列表， ##

类似java中的List的contains方法

    if 1 in aa:
      print 'Very Good'
    else:
      print 'Not Bad'

这里是判断 1 是否在 aa 内部


## 可以用来判断字符串是否包含某一串 ##

,可以用来筛选文件使用

    if 'a' in 'qa'
      print 'ok'

---
## in ##

in	如果在指定的序列中找到值返回 True，否则返回 False。	x 在 y 序列中 , 如果 x 在 y 序列中返回 True。

not in	如果在指定的序列中没有找到值返回 True，否则返回 False。	x 不在 y 序列中 , 如果 x 不在 y 序列中返回 True。

---
## is ##

is	is 是判断两个标识符是不是引用自一个对象	x is y, 类似 id(x) == id(y) , 如果引用的是同一个对象则返回 True，否则返回 False

is not	is not 是判断两个标识符是不是引用自不同对象	x is not y ， 类似 id(a) != id(b)。如果引用的不是同一个对象则返回结果 True，否则返回 False。

————————————————
版权声明：本文为CSDN博主「zhangvalue」的原创文章，遵循CC 4.0 BY-SA版权协议，转载请附上原文出处链接及本声明。
原文链接：https://blog.csdn.net/zhangvalue/article/details/94598781


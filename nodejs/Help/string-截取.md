# 字符串截取 #

## substring（ start ,stop ） ##

 它是用来截取指定下标之间的字符，并且返回的字串包括 start 处的字符，但不包括 stop 处的字符

    var oldString="tongyuwan"；
    var newString1=oldString.substring(4,6);

结果如下：

    newString1=“yu”


----------

## substr(start,length) ##

 它是用来截取从某位开始，截取多少位的字符串

    var oldString="tongyuwan"；
    var newString=oldString.substr(4,5);
    
    结果如下：
    newString=“yuwan”
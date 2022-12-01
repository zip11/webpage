# XCOPY只拷贝当天文件的实现代码 #

----------

## 获取 系统时间 ##
    echo %date% 

::2022/11/30 周三

中国日期格式 年-月-日

    :: year 
    echo %date:~0,4% 
    
    :: month
    echo %date:~5,2%
    
    :: day
    echo %date:~8,2%
    

----------


    ::bat
    
    set nian=%date:~0,4
    
    set yue=%date:~5,2%
    
    set ri=%date:~8,2%
    
    xcopy c:\source\*.* e:\dest /d:%yue%-%ri%-%nian%

----------

XCOPY使用了 /D:mm-dd-yyyy参数，即只拷贝指定日期之后的文件，那当天日期如何生成的呢，使用了%date% 取得系统日期，如果是一般的中文XP系统，日期格式是YYYY-MM-DD，

所以就用截取字符串的方式重造了美国日期格式。如：%date:~0,4% 表示截取从第0位开始截取长度4个字符从而得到YYYY（年），如：%date:~5,5% 表示截取从第5位开始截取长度5个字符从而得到MM-DD（月-日）

重塑美国日期变量格式 “月-日-年”，只选择拷贝当前日期的文件





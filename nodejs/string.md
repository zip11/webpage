## 子字符串搜索 ##

    stringObject.indexOf(searchvalue,fromindex)
    
返回某个指定的字符串值在字符串中首次出现的位置

参数	描述


- searchvalue	必需。规定需检索的字符串值。


- fromindex	可选的整数参数。规定在字符串中开始检索的位置。它的合法取值是 0 到 stringObject.length - 1。如省略该参数，则将从字符串的首字符开始检索

    var str="Hello world!"

    document.write(str.indexOf("Hello") + "<br />")


## 字符串分割 ##

    // Initialize string 
    var str = "Welcome*to*GeeksforGeeks"; 

    var string = str.split("*"); 

输出：

    [ 'Welcome', 'to', 'GeeksforGeeks' ]

## 字符串 删除 字符串 ##

    // Initialize string 
    var str = "Welcome*to*GeeksforGeeks"; 
    str.replace("\r\n","")
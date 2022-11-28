[http://c.biancheng.net/view/4305.html](http://c.biancheng.net/view/4305.html)

Python 3.x 默认采用 UTF-8 编码格式，有效地解决了中文乱码的问题。

在 Python 中，有 2 种常用的字符串类型，分别为 str 和 bytes 类型，其中 str 用来表示 Unicode 字符，bytes 用来表示二进制数据。str 类型和 bytes 类型之间就需要使用 encode() 和 decode() 方法进行转换。

# encode()方法 #

encode() 方法为字符串类型（str）提供的方法，用于将 str 类型转换成 bytes 类型，这个过程也称为“编码”。

    str.encode([encoding="utf-8"][,errors="strict"])
    

----------

# decode()方法 #

Python decode()方法 和 encode() 方法正好相反，
decode() 方法用于将 bytes 类型的二进制数据转换为 str 类型，这个过程也称为“解码”。

    bytes.decode([encoding="utf-8"][,errors="strict"])
    
    >>> str = "C语言中文网"
    >>> bytes=str.encode()
    
    >>> bytes.decode()
    'C语言中文网'
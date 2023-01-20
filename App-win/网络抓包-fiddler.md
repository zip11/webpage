# 抓包工具：fiddler和wireshark对比 #

[https://zhuanlan.zhihu.com/p/44912855](https://zhuanlan.zhihu.com/p/44912855)

抓包就是将网络传输发送与接收的数据包进行截获、重发、编辑、转存等操作，也用来检查网络安全。抓包也经常被用来进行数据截取等。


最常用的2种。

Fiddler是在windows上运行的程序，专门用来捕获HTTP，HTTPS的。

wireshark能获取HTTP，也能获取HTTPS，但是不能解密HTTPS，所以wireshark看不懂HTTPS中的内容。

总结，如果是处理HTTP,HTTPS 还是用Fiddler, 其他协议比如TCP,UDP 就用wireshark。

## 一、Fiddler ##

当启动fiddler，程序将会把自己作为一个代理，所以的http请求在达到目标服务器之前都会经过fiddler，同样的，所有的http响应都会在返回客户端之前流经fiddler。

Fiddler可以抓取支持http代理的任意程序的数据包，如果要抓取https会话，要先安装证书。

Fiddler的工作原理

Fiddler 是以代理web服务器的形式工作的,它使用代理地址:127.0.0.1, 端口:8888. 当Fiddler会自动设置代理， 退出的时候它会自动注销代理，这样就不会影响别的程序。不过如果Fiddler非正常退出，这时候因为Fiddler没有自动注销，会造成网页无法访问。解决的办法是重新启动下Fiddler


## Fiddler如何捕获HTTPS会话 ##

默认下，Fiddler不会捕获HTTPS会话，需要你设置下, 打开Fiddler Tool->Fiddler Options->HTTPS tab



## QuickExec命令行的使用 ##

Fiddler的左下角有一个命令行工具叫做QuickExec,允许你直接输入命令。

常见得命令有：

help 打开官方的使用页面介绍，所有的命令都会列出来

cls 清屏 (Ctrl+x 也可以清屏)

select 选择会话的命令

.png 用来选择png后缀的图片

bpu 截获request



## Fiddler中设置断点修改Request ##

Fiddler最强大的功能莫过于设置断点了，设置好断点后，你可以修改httpRequest 的任何信息包括host, cookie或者表单中的数据。设置断点有两种方法

第一种：打开Fiddler 点击Rules-> Automatic Breakpoint ->Before Requests(这种方法会中断所有的会话)

如何消除命令呢？ 点击Rules-> Automatic Breakpoint ->Disabled

第二种: 在命令行中输入命令: bpu http://www.baidu.com (这种方法只会中断http://www.baidu.com)

如何消除命令呢？ 在命令行中输入命令 bpu
# 二、Wireshark #


Wireshark是另外一种抓包工具，这种工具比fiddler更强大，消息量更多。大家可能会问：有了fiddler，为什么还要用wireshark呢？这里说下，在测试中，发现用fiddler抓包，有些包是没有抓到的，比如在验证反作弊信息的时候，反作弊pingback信息的消息用fiddler就没抓到，用wireshark就抓到了。还有另外一种情况，就是在验证cna的时候，如果先用fiddler抓包，如果没有种下cna的时候，以后就永远没有cna了，情况很诡异。解决办法就是把包卸载了重新安装，第一次用wireshark抓包。

Wireshark优势：

1、强大的协议解析能力，一到七层全解码，一览无遗，对于协议细节的研究特别有帮助。

2、对于https加密流量，只要将浏览器的session key 自动导入wireshark，Wireshark可以自动解密https流量。

Wireshark不足之处：

尽管可以自定义过滤列表，但为了抓取一个特定TCP Flow /Session 流量需要写一个长长的过滤列表，这对于初学者很不友好。

## 操作实例： ##

wireshark是捕获机器上的某一块网卡的网络包，当你的机器上有多块网卡的时候，你需要选择一个网卡。



点击Caputre->Interfaces.. 出现下面对话框，选择正确的网卡。然后点击"Start"按钮, 开始抓包：


### 一、WireShark 界面 ###


1、Display Filter(显示过滤器)，用于过滤；

2、Packet List Pane(封包列表)，显示捕获到的封包，有源地址和目标地址,端口号；

3、Packet Details Pane(封包详细信息), 显示封包中的字段；

4、Dissector Pane(16进制数据)；

5、Miscellanous(地址栏，杂项)。

### 二、Wireshark 显示过滤 ###

使用过滤是非常重要的，初学者使用wireshark时，将会得到大量的冗余信息，在几千甚至几万条记录中，以至于很难找到自己需要的部分。搞得晕头转向。过滤器会帮助我们在大量的数据中迅速找到我们需要的信息。

过滤器有两种:

1、一种是显示过滤器，就是主界面上那个，用来在捕获的记录中找到所需要的记录

2、一种是捕获过滤器，用来过滤捕获的封包，以免捕获太多的记录。 在Capture -> Capture Filters 中设置。

三、保存过滤

在Filter栏上，填好Filter的表达式后，点击Save按钮， 取个名字。比如"Filter 102",Filter栏上就多了个"Filter 102" 的按钮。

四、过滤表达式的规则

表达式规则

1.协议过滤 比如TCP，只显示TCP协议。

2.IP 过滤

比如 ip.src ==192.168.1.102 显示源地址为192.168.1.102，ip.dst==192.168.1.102,目标地址为192.168.1.102。

3.端口过滤

tcp.port ==80, 端口为80的

tcp.srcport == 80, 只显示TCP协议的愿端口为80的。

4.Http模式过滤

http.request.method=="GET", 只显示HTTP GET方法的。

5.逻辑运算符为 AND/ OR

## 五、封包列表(Packet List Pane) ##

封包列表的面板中显示，编号，时间戳，源地址，目标地址，协议，长度，以及封包信息。 你可以看到不同的协议用了不同的颜色显示。 你也可以修改这些显示颜色的规则， View ->Coloring Rules.

六、封包详细信息 (Packet Details Pane)

这个面板是我们最重要的，用来查看协议中的每一个字段。各行信息分别为

·Frame: 物理层的数据帧概况

·Ethernet II: 数据链路层以太网帧头部信息

·Internet Protocol Version 4: 互联网层IP包头部信息

·Transmission Control Protocol: 传输层T的数据段头部信息，此处是TCP

·Hypertext Transfer Protocol: 应用层的信息，此处是HTTP协议

七、Wireshark与对应的OSI七层模型


### 八、TCP包的具体内容 ###

从下图可以看到wireshark捕获到的TCP包中的每个字段。
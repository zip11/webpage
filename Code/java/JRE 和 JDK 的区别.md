## JRE： Java Runtime Environment ##

JRE顾名思义是java运行时环境，包含了java虚拟机，java基础类库。是使用java语言编写的程序运行所需要的软件环境，是提供给想运行java程序的用户使用的。JDK顾名思义是java开发工具包，是程序员使用java语言编写java程序所需的开发工具包，是提供给程序员使用的。

JRE根据不同操作系统（如：windows，linux等）和不同JRE提供商（IBM,ORACLE等）有很多版本，最常用的是Oracle公司收购SUN公司的JRE版本。如果你想查看更官方的解释，可以前往


## JDK：Java Development Kit  ##

JDK包含了JRE，同时还包含了编译java源码的编译器javac，

还包含了很多java程序调试和分析的工具：jconsole，jvisualvm等工具软件，还包含了java程序编写所需的文档和demo例子程序。如果你需要运行java程序，只需安装JRE就可以了。如果你需要编写java程序，需要安装JDK。


## JVM ##


JVM就是我们常说的java虚拟机，它是整个java实现跨平台的最核心的部分，所有的java程序会首先被编译为.class的类文件，这种类文件可以在虚拟机上执行，也就是说class并不直接与机器的操作系统相对应，而是经过虚拟机间接与操作系统交互，由虚拟机将程序解释给本地系统执行。
 
可以理解为是一个虚拟出来的计算机，具备着计算机的基本运算方式，它主要负责将java程序生成的字节码文件解释成具体系统平台上的机器指令。让具体平台如window运行这些Java程序。 


![](http://https://img-blog.csdn.net/20160614105103329?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQv/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/Center)






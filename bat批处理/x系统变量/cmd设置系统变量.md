## 使用cmd设置环境变量 ##

默认情况下写入的是用户变量，要想写环境变量，加 /M
例如

### 需要以管理员启动cmd ###

    setx /M key value

### 需要引用 旧值 ###

    setx PATH "%PATH%;D:\Program Files\"

----------

# jdk添加系统变量 #


- 新建“JAVA_HOME”系统变量

    C:\Program Files\Java\jdk1.8.0_333


- 新建“CLASSPATH”系统变量


    .;%JAVA_HOME%\lib;%JAVA_HOME%\lib\dt.jar;%JAVA_HOME%\lib\tools.jar;



- 系统变量”下的“Path”变量

  Path界面，新建变量，值为 %JAVA_HOME%\bin

  Path界面，新建变量，值为 %JAVA_HOME%\jre\bin
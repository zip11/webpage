# Python3 venv简单使用——创建虚拟环境 #

---

在使用Python的时候，有的时候又希望安装的相关依赖不影响原来的系统配置。这个时候就需要用到venv（Virtualenv）创建虚拟的Python环境，以供使用。

在Python3.3中使用”venv”命令创建的环境不包含”pip”，你需要进行手动安装。但是只有版本在3.3之上都没有问题啦。

## 设置 虚拟环境 路面 ##

我们先在某个目录下（最后是根目录或者是桌面，关键是下次要用能够找得到），输入：

    $ python -m venv XXX


XXX指你要创建的文件名。因为在执行这行命令之后，就会把与Python虚拟环境有关的文件放到XXX里面。

## 激活 虚拟环境 ##

之后只需要运行这个里面的activate文件就行。

Linux下的命令如下：

    $ source <XXX>/bin/activate


Windows的cmd下是：

    C:> <XXX>/Scripts/activate.bat

在PowerShell下是：

    PS C:> <venv>/Scripts/Activate.ps1

但是为了避免运行不信任的脚本，PowerShell下此脚本可能被禁止。此时输入命令：

    set-executionpolicy remotesigned

然后更改执行策略就可以了。


## 退出 虚拟环境 ##

    $ deactivate
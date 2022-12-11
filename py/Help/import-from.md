# import as from import 区别 #

在python中import或者from…import是用来导入相应的模块。那每一种有什么具体的差别呢？


## 一、import ##

只有import，为最简单的引入对应的包。例如：

import pickle #引入 pickle包

import os #引入 os包


## 二、from A import B ##

这种方式意味着从A中引入B。相当于：import A， b=A.b。

from urllib.parse import urlparse

from sys import argv


除了这种基本形式，还有另外两种，例如：

from os import makedirs, unlink, sep #从os包中引入 makedirs.unlink,sep类

from os import listdir, getcwd #从os包中引入 listdir, getcwd 类

from os.path import dirname, exists, isdir, splitext #从 os包中的path类中引入 dirmame exists 方法

from os.path import join #从 os包中的path类中引入 join 方法


## 三、import A as B ##



这种方式为给引入的包A定义一个别名B，例如：

import xml.etree.ElementTree as ET #给包xml.etree.ElementTree 定义一个 ET 别名
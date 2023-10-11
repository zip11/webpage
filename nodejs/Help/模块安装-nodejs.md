# 模块安装-nodejs #

---

## 1. 安装全局模块 ##

-g 参数的意义

 npm install -g express 

-g 参数代表着全局，英文单词 global，使用 -g 参数安装的是全局模块。-g 可以写在要安装的包前面或后面位置。

全局模块安装到了哪里？
// 输入指令查询全局模块安装路径
$ npm list -g --depth=0


## 2. 安装本地模块 ##

不使用 -g 参数安装的模块都会安装到本地模块。
$ npm install path

本地模块安装在当前目录下的 node_modules 目录下。


## 3. 安装指定版本的模块 ##

前提是要知道具体的版本号，如果不知道，可以使用 @3.* 表示安装第三版中最新的包。


## 4. 同时安装多个模块 ##

有时候需要安装多个模块，一个个安装太过麻烦，可以一起安装，模块之间以空格隔开即可。

如下为同时安装 antd 模块和 babel-plugin-import 模块。

$ npm install antd babel-plugin-import 


## 5. 安装 package.json 中的包 ##

package.json 文件其中一个重要功能就是记录当前项目的依赖包有哪些。

这样在下载完一个项目时；
查看 package.json 可以知道项目依赖哪些包；
使用 npm install 指令可以安装 package.json 中记录的依赖包；
安装完依赖包，才可以启动项目把项目给跑起来。

$ npm install   // 就是这么简单，当然前提是有 package.json 并且里面配置了相关包信息

##  --save 的用途 ##
--save 和 -g 一样，属于参数。

在安装模块时，只有当事人知道安装了哪些模块，如果换另外一个人来看这个项目，是不会知道这个项目安装了哪些模块。

使用 --save 可以在安装模块时，同时将安装的模块信息记录在 package.json 文件中，这样第三个人再看这个项目时，就可以直接看 package.json 文件来了解这个项目依赖了哪些包。

$ npm install antd --save


## --save-dev 的用途 ##

与 --save 参数类似，--save-dev 也会将模块信息记录到 package.json 文件中，不同的是记录在文件中的 devDependencies 属性下。
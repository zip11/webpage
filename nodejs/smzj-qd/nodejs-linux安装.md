## 安装 nodejs ##
    sudo apt-get update 
    
    sudo apt-get install nodejs

## 卸载nodejs ##

    #卸载nodejs
    sudo apt-get remove nodejs

    #清除软件包以及相关配置
    sudo apt-get purge nodejs

### 查看版本 ###
    node -v

pi3

v10.24.0

## nvm安装 ##

灵活安装 特定版本

[https://raspberrypi.club/307.html](https://raspberrypi.club/307.html)


----------


##  手动安装 lts 18.12.1 指定版本 ##

官网下载

[https://nodejs.org/zh-cn/download/](https://nodejs.org/zh-cn/download/)

arm v7版本

[https://nodejs.org/dist/v18.12.1/node-v18.12.1-linux-armv7l.tar.xz](https://nodejs.org/dist/v18.12.1/node-v18.12.1-linux-armv7l.tar.xz)

	# 新建 下载文件夹
    mkdir ~/nodejs
	# 下载 程序
    wget https://nodejs.org/dist/v18.12.1/node-v18.12.1-linux-armv7l.tar.xz


    # 首先在/usr/local/lib创建一个文件夹
    sudo mkdir /usr/local/lib/nodejs

    # 将安装包解压到新创建的文件夹里面
    sudo tar -xJvf ~/nodejs/node-v18.12.1-linux-armv7l.tar.xz -C /usr/local/lib/nodejs


## 创建软链接 ##

    #node
    sudo ln -s /usr/local/lib/nodejs/node-v18.12.1-linux-armv7l/bin/node /usr/bin/node

    #npm
    sudo ln -s /usr/local/lib/nodejs/node-v18.12.1-linux-armv7l/bin/npm /usr/bin/npm

    #npx
    sudo ln -s /usr/local/lib/nodejs/node-v18.12.1-linux-armv7l/bin/npx /usr/bin/npx

## 检测是否安装成功 ##


    node -v
    # 输出v10.16.0则代表安装成功
    # npm、npx同上